"""
Execute the command on the device
"""

from .executor import Centos72Executor

EXECUTOR_MAP = {
    "centos72": Centos72Executor
}
