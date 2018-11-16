import paramiko

class SshConnector(object):

    def __init__(self, device):
        self.ip = device.ip
        self.port = device.port
        self.user = device.user
        self.password = device.password
        self.protocol = device.protocol
        self.device = device

    def send_cmd_executor(self, cmd):
        self.device.executor.check_cmd(cmd)
        return self.device.executor.execute(cmd)

    def make_connect(self):
        # todo
        # should add some boundary judgment
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.ip, self.port, self.user, self.password)

    def close_connect(self):
        pass


class TelnetConnector(object):
    pass