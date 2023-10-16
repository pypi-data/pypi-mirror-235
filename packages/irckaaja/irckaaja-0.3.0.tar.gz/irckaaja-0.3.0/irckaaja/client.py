import time
from threading import Thread
from typing import Dict, List, Optional, cast

from irckaaja.channel import IrcChannel
from irckaaja.config import BotConfig, ScriptConfig, ServerConfig
from irckaaja.connection import IrcConnection
from irckaaja.dynamicmodule import DynamicModule
from irckaaja.protocol import (
    ChannelMessage,
    CTCPVersionMessage,
    EndOfMotdMessage,
    JoinMessage,
    MessageType,
    ParsedMessage,
    PartMessage,
    PingMessage,
    PrivateMessage,
    QuitMessage,
    TopicMessage,
    TopicReplyMessage,
    User,
    UsersEndMessage,
    UsersMessage,
)


class IrcClient:
    """
    IRC Client
    """

    PING_INTERVAL_THRESHOLD = 300  # 300 seconds

    def __init__(
        self,
        server_config: ServerConfig,
        bot_config: BotConfig,
        modules_config: Dict[str, ScriptConfig],
    ) -> None:
        self.alive = True
        self.connected = False
        self.server_config = server_config
        self.bot_config = bot_config
        self.networkname = server_config.name

        self._reader_thread = Thread(target=self._connection_loop)
        self._connection = IrcConnection(
            self.server_config.hostname,
            self.server_config.port,
            self.server_config.use_tls,
            self.server_config.ca_path,
        )

        self._channel_list: List[IrcChannel] = []

        self.modules_config = modules_config
        self.dynamic_modules: List[DynamicModule] = [
            DynamicModule(self, script_config.module_name, script_config.config)
            for script_config in modules_config.values()
        ]

        self._last_ping = time.monotonic()

    def _route_message(self, parsed: ParsedMessage) -> None:
        type = parsed.type

        if parsed.message is None:
            self._unknown_message_received(parsed.raw_message or "")
            return

        if type == MessageType.PRIVATE_MESSAGE:
            self._private_message_received(cast(PrivateMessage, parsed.message))
        elif type == MessageType.JOIN:
            self._join_received(cast(JoinMessage, parsed.message))
        elif type == MessageType.PART:
            self._part_received(cast(PartMessage, parsed.message))
        elif type == MessageType.PING:
            self._ping_received(cast(PingMessage, parsed.message))
        elif type == MessageType.QUIT:
            self._quit_received(cast(QuitMessage, parsed.message))
        elif type == MessageType.TOPIC:
            self._topic_received(cast(TopicMessage, parsed.message))
        elif type == MessageType.END_OF_MOTD:
            self._motd_received(cast(EndOfMotdMessage, parsed.message))
        elif type == MessageType.TOPIC_REPLY:
            self._topic_reply_received(cast(TopicReplyMessage, parsed.message))
        elif type == MessageType.USERS:
            self._users_received(cast(UsersMessage, parsed.message))
        elif type == MessageType.END_OF_USERS:
            self._users_end_received(cast(UsersEndMessage, parsed.message))
        elif type == MessageType.CHANNEL_MESSAGE:
            self._channel_message_received(cast(ChannelMessage, parsed.message))
        elif type == MessageType.CTCP_VERSION:
            self._ctcp_version_received(
                cast(CTCPVersionMessage, parsed.message)
            )
        elif type in [
            MessageType.CTCP_TIME,
            MessageType.CTCP_VERSION,
            MessageType.CTCP_PING,
            MessageType.CTCP_DCC,
        ]:
            self._ctcp_message_received()

    def connect(self) -> None:
        """
        Non-blocking method that initiates connection.
        """
        self._reader_thread = Thread(target=self._connection_loop)
        self._reader_thread.start()

    def _connect(self) -> None:
        while self.alive:
            try:
                self._connection.close()
                self._connection = IrcConnection(
                    self.server_config.hostname,
                    self.server_config.port,
                    self.server_config.use_tls,
                    self.server_config.ca_path,
                )
                self._connection.connect()

                self.set_nick(self.bot_config.nick)
                self.set_user(
                    self.bot_config.username, self.bot_config.realname
                )

                self._last_ping = time.monotonic()
                break

            except Exception as e:
                self._print_line(str(e) + " " + self.server_config.hostname)
                self._print_line("Trying again in 30 seconds.")
                self._sleep(30)

    def _connection_loop(self) -> None:
        while self.alive:
            self._connect()
            self._process()

            if not self.alive:
                break

            self._print_line("Trying again in 60 seconds.")
            self._sleep(60)

    def _write(self, message: str) -> None:
        """
        Prints and writes message to server.
        """
        self._print_line(message[:-1])
        self._connection.write(message)

    def _check_ping_time(self) -> bool:
        return (
            time.monotonic() - self._last_ping
            < IrcClient.PING_INTERVAL_THRESHOLD
        )

    def _process(self) -> None:
        """
        Reads and handles messages.
        """
        while self.alive and self._check_ping_time():
            try:
                messages = self._connection.read()
            except (OSError, EOFError) as e:
                self._print_line(str(e))
                break

            if not self.alive:
                break

            self._handle_messages(messages)

        self._connection.close()
        self._print_line("Connection closed.")
        self.connected = False

    def _handle_messages(self, messages: List[ParsedMessage]) -> None:
        """
        Handles a list of messages
        """
        for message in messages:
            self._route_message(message)

    def _print_line(self, message: str) -> None:
        """
        Prints message with timestamp.
        """
        print(
            time.strftime("%H:%M:%S") + " |" + self.networkname + "| " + message
        )

    def set_nick(self, nick: str) -> None:
        """
        Sets user's nick on server.
        """
        self._write("NICK " + nick + "\r\n")

    def set_user(self, username: str, realname: str) -> None:
        """
        Sets username and realname to server on connect.
        """
        self._write("USER " + username + " 0 * :" + realname + "\r\n")

    def send_pong(self, message: str) -> None:
        """
        Reply to PING.
        """
        self._write("PONG :" + message + "\r\n")

    def join_channel(self, channel: str) -> None:
        """
        Joins a irc channel.
        """
        self._write("JOIN :" + channel + "\r\n")

    def leave_channel(self, channel: str, reason: str = "") -> None:
        """
        PARTs from a channel.
        """
        msg = "PART " + channel
        if reason:
            msg += " :" + reason
        self._write(msg + "\r\n")

    def send_privmsg(self, target: str, message: str) -> None:
        """
        Sends PRIVMSG to target.
        """
        self._write("PRIVMSG " + target + " :" + message + "\r\n")

    def send_ping(self, message: str) -> None:
        """
        Sends PING to server.
        """
        self._write("PING " + message + "\r\n")

    def send_CTCP(self, target: str, message: str) -> None:
        self.send_privmsg(target, str("\x01" + message + "\x01"))

    def send_notice(self, target: str, message: str) -> None:
        self._write("NOTICE " + target + " :" + message + "\r\n")

    def _on_connect(self) -> None:
        """
        Called when connected to the network.
        """
        self.send_ping(self.server_config.hostname)
        self._join_channels()

        for dm in self.dynamic_modules:
            try:
                dm.instance.on_connect()
            except Exception as e:
                print(e)

    def _join_channels(self) -> None:
        """
        Joins channels specified in server_config.
        """
        for channel in self.server_config.channels:
            self.join_channel(channel)

    def kill(self) -> None:
        """
        Called when the thread is wanted dead.
        """
        self.alive = False
        for m in self.dynamic_modules:
            m.instance.kill()

    def _private_message_received(self, msg: PrivateMessage) -> None:
        """
        Called when a private message has been received. Prints it
        and calls on_private_message() on BotScript instances.
        """
        source = msg.source.nick
        message = msg.message
        self._print_line("PRIVATE" + " <" + source + "> " + message)

        for dm in self.dynamic_modules:
            try:
                dm.instance.on_private_message(msg.source, message)
            except Exception as e:
                print(e)

    def _channel_message_received(self, msg: ChannelMessage) -> None:
        """
        Called when a PRIVMSG to a channel has been received. Prints it
        and calls on_channel_message() on BotScript instances.
        """
        source = msg.source.nick
        message = msg.message
        msg.source.full_mask
        channel = msg.channel

        self._print_line(channel + " <" + source + "> " + message)

        for dm in self.dynamic_modules:
            try:
                dm.instance.on_channel_message(msg.source, channel, message)
            except Exception as e:
                print(e)

    def _ping_received(self, msg: PingMessage) -> None:
        """
        Called when PING message has been received.
        """

        self._last_ping = time.monotonic()
        message = msg.message
        self.send_pong(message)

    def _motd_received(self, msg: EndOfMotdMessage) -> None:
        """
        Called when the end of MOTD message
        has been received.
        """
        message = msg.message

        self._print_line(message)
        if not self.connected:
            self.connected = True
            self._on_connect()

    def _find_channel_by_name(self, channel_name: str) -> Optional[IrcChannel]:
        """
        Returns a channel instance from channel_list
        matching channel_name parameter or None.
        """
        for channel in self._channel_list:
            if channel.name == channel_name:
                return channel
        return None

    def _add_channel(self, name: str, user_list: List[str]) -> None:
        """
        Adds a channel to networks channel list.
        """
        if self._find_channel_by_name(name):
            return

        channel = IrcChannel(name, user_list)
        self._channel_list.append(channel)

    def _users_received(self, msg: UsersMessage) -> None:
        """
        Called when USERS message is received. Notifies
        channel instance of the users.
        """

        channel_name = msg.channel
        user_list = msg.users

        channel = self._find_channel_by_name(channel_name)
        if not channel:
            self._add_channel(channel_name, user_list)
            return

        channel.users_message(user_list)

    def _users_end_received(self, msg: UsersEndMessage) -> None:
        """
        Called when USERS message's end has been received.
        Notifies the channel instance.
        """

        channel_name = msg.channel

        channel = self._find_channel_by_name(channel_name)
        if not channel:
            # TODO FIX
            self._print_line("REPORT THIS: usersEndReceived, channel not found")
            return

        channel.users_message_end()
        self._print_line("USERS OF " + channel_name)
        self._print_line(" ".join(channel.userlist))

    def _quit_received(self, msg: QuitMessage) -> None:
        """
        Called when a QUIT message has been received. Calls
        on_quit() on BotScripts
        """

        for channel in self._channel_list:
            channel.remove_user(msg.user.nick)

        self._print_line(msg.user.nick + " has quit.")

        for dm in self.dynamic_modules:
            try:
                dm.instance.on_quit(msg.user)
            except Exception as e:
                print(e)

    def _part_received(self, msg: PartMessage) -> None:
        """
        Called when a PART message has been received. Calls
        on_part() on BotScripts
        """

        channel_name = msg.channel
        nick = msg.user.nick
        msg.user.full_mask

        channel = self._find_channel_by_name(channel_name)
        if not channel:
            return

        channel.remove_user(nick)

        self._print_line(nick + " has parted " + channel_name)

        for dm in self.dynamic_modules:
            try:
                dm.instance.on_part(msg.user, channel_name)
            except Exception as e:
                print(e)

    def _join_received(self, msg: JoinMessage) -> None:
        """
        Called when a JOIN message has been received. Calls
        on_join() on BotScripts
        """

        nick = msg.user.nick
        channel_name = msg.channel
        msg.user.full_mask

        channel = self._find_channel_by_name(channel_name)
        if channel:
            channel.add_user(nick)

        self._print_line(nick + " has joined " + channel_name)
        for dm in self.dynamic_modules:
            try:
                dm.instance.on_join(msg.user, channel_name)
            except Exception as e:
                print(e)

    def _topic_received(self, msg: TopicMessage) -> None:
        """
        Called when topic is changed on a channel. Calls on_topic()
        on BotScripts
        """

        nick = msg.user.nick
        channel_name = msg.channel
        topic = msg.topic

        channel = self._find_channel_by_name(channel_name)
        if channel:
            channel.topic = topic

        self._print_line(
            nick + " changed the topic of " + channel_name + " to: " + topic
        )
        for dm in self.dynamic_modules:
            try:
                dm.instance.on_topic(msg.user, channel_name, topic)
            except Exception as e:
                print(e)

    def _topic_reply_received(self, msg: TopicReplyMessage) -> None:
        """
        Called when server responds to client's /topic or server informs
        of the topic on joined channel.
        """

        channel_name = msg.channel
        topic = msg.topic

        channel = self._find_channel_by_name(channel_name)
        if channel:
            channel.topic = topic

        self._print_line("Topic in " + channel_name + ": " + topic)
        for dm in self.dynamic_modules:
            try:
                dm.instance.on_topic(User(msg.nick, ""), channel_name, topic)
            except Exception as e:
                print(e)

    def _ctcp_message_received(
        self,
    ) -> None:
        self._print_line("CTCP")

    def _ctcp_version_received(self, msg: CTCPVersionMessage) -> None:
        ":juke!juke@jukk.is NOTICE irckaaja :VERSION ?l? hakkeroi!"
        self.send_notice(msg.user.nick, "\x01VERSION irckaaja 0.1.0\x01")

    def _unknown_message_received(self, msg: str) -> None:
        self._print_line(msg)

    def _sleep(self, seconds: float) -> None:
        """
        Sleeps for seconds unless not self.alive.
        """
        start = time.monotonic()
        while time.monotonic() < start + seconds and self.alive:
            time.sleep(1)
