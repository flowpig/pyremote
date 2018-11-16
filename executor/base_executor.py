class BaseExecutor(object):

    def __init__(self, connector):
        self.connector = connector

    def check_cmd(self, cmd):
        pass

    def execute(self, cmd):
        stdin, stdout, stderr = self.connector.ssh.exec_command(cmd)
        return stdout.read()