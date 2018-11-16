from .base_linux import BaseLinux
from ..executor import EXECUTOR_MAP

class SystemCent72(BaseLinux):
    DEVICE = "centos72"

    def _create_executor(self):
        """
        create executor
        :return:
        """
        if self.DEVICE in EXECUTOR_MAP:
            self.executor = EXECUTOR_MAP[self.DEVICE](self.connector)
        else:
            raise Exception('device not support')
