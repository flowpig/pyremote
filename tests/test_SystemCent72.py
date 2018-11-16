import sys
sys.path.append('..')
from pyremote.device import SystemCent72

def test_system_cent72():
    centos72 = SystemCent72(ip="xxx.xxx.xxx.xxx", port=22, user="xxx", password="xxx", protocol="ssh")
    result = centos72.cmd_run("df -h")
    assert result != ''