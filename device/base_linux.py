from ..connector import CONNECTOR_MAP


class BaseLinux(object):

    def __init__(self, ip, port, user, password, protocol):
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password
        self.protocol = protocol

    def _init_handle(self):
        """
        make pre run logic
        :return:
        """
        self._create_connector()
        self._create_executor()

    def cmd_run(self, cmd):
        self._init_handle()
        self.connector.make_connect()
        result = self.connector.send_cmd_executor(cmd)
        return result

    def _create_connector(self):
        """
        create connector [ssh, telnet, ...]
        :return: connector object
        """
        if self.protocol in CONNECTOR_MAP:
            self.connector = CONNECTOR_MAP[self.protocol](self)
        else:
            raise Exception('protocol not support')

    def _create_executor(self):
        """
        create executor
        :return:
        """
        pass

    def handle_result(self):
        """
        reference adaptor to handle executor result
        :return:
        """
        pass
