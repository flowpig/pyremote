""""
Make a network connection
"""

from .connector import SshConnector, TelnetConnector

CONNECTOR_MAP = {
    "ssh": SshConnector,
    "telnet": TelnetConnector
}
