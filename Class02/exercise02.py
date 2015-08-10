#!/usr/bin/env python

import telnetlib
import time
import socket
import sys

TELNET_PORT = 23
TELNET_TIMEOUT = 6
SLEEP_TIME = 1

def telnet_connect(ip_addr, port=TELNET_PORT, timeout=TELNET_PORT):
    try:
        return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    except socket.timeout:
        sys.exit("Connection timed-out")

def login(remote_conn, username, password, timeout=TELNET_TIMEOUT, sleep=SLEEP_TIME):
    output = remote_conn.read_until("sername:", timeout)
    remote_conn.write(username + "\n")
    output += remote_conn.read_until("assword:", timeout)
    remote_conn.write(password + "\n")
    time.sleep(SLEEP_TIME)
    output += remote_conn.read_very_eager()
    return '\n'.join(output.split('\n')[1:-1])

def send_command(remote_conn, cmd, sleep=SLEEP_TIME):
    cmd = cmd.rstrip()
    remote_conn.write(cmd + "\n")
    time.sleep(sleep)
    return '\n'.join(remote_conn.read_very_eager().split('\n')[1:-1])

def main():
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    password = '88newclass'

    remote_conn = telnet_connect(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    login(remote_conn, username, password)
    
    output = send_command(remote_conn, "terminal length 0")
    output = send_command(remote_conn, "show ip interface brief")
    print output

    remote_conn.close()


if __name__ == "__main__":
    main()