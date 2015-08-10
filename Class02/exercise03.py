#!/usr/bin/env python

import telnetlib
import socket
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 6
SLEEP_TIME = 1

class TelnetConn(object):
    """
    A telnet connection class to simplify use of telnetlib.
    """
    def __init__(self, ip_addr, port=TELNET_PORT, timeout=TELNET_TIMEOUT):
        self.timeout = timeout
        self.sleep = SLEEP_TIME
        try:
            self.connection = telnetlib.Telnet(ip_addr, port, timeout)
        except socket.timeout:
            return None
        except socket.error:
            return None
    
    def login(self, username, password):
        """
        Login with the given credentials.
        """
        self.connection.read_until("sername:", self.timeout)
        self.connection.write(username + "\n")
        self.connection.read_until("assword:", self.timeout)
        self.connection.write(password + "\n")
        time.sleep(self.sleep)
        self.connection.read_very_eager()
    
    def send_command(self, command=""):
        """
        Send a command via telnet. Return the response.
        """
        self.connection.write(command.strip() + "\n")
        time.sleep(self.sleep)
        return '\n'.join(self.connection.read_very_eager().split('\n')[1:-1])
        
    def disable_paging(self, command="terminal length 0"):
        """
        Disable the paging of the output.
        """
        return self.send_command(command)
    
    def close(self):
        """
        Close the connection.
        """
        return self.connection.close()


if __name__ == "__main__":
    
    t = TelnetConn('50.76.53.27')
    t.login('pyclass', '88newclass')
    t.disable_paging()
    output = t.send_command('show ip interface brief')
    print output
    t.close()
