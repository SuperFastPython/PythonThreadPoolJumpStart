# SuperFastPython.com
# scan a range of port numbers on host one by one,
from socket import AF_INET
from socket import SOCK_STREAM
from socket import socket

# returns True if can connect, False otherwise
def test_port_number(host, port):
    # create and configure the socket
    with socket(AF_INET, SOCK_STREAM) as sock:
        # set a timeout of a few seconds
        sock.settimeout(3)
        # connecting may fail
        try:
            # attempt to connect
            sock.connect((host, port))
            # a successful connection was made
            return True
        except:
            # ignore the failure
            return False

# scan port numbers on a host
def port_scan(host, ports):
    print(f'Scanning {host}...')
    # scan each port number
    for port in ports:
        if test_port_number(host, port):
            print(f'> {host}:{port} open')

# protect the entry point
if __name__ == '__main__':
    # define host and port numbers to scan
    host = 'python.org'
    ports = range(1024)
    # test the ports
    port_scan(host, ports)
