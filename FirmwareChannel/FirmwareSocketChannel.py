from FirmwareChannel import FirmwareChannel as FC
import socket

class FirmwareSocketChannel(FC.FirmwareChannel):

    def __init__(self, portNumber=6144):
        self.portNumber = portNumber
        self.PACKET_BUFFER_SIZE = 1024
        self.mbedSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.mbedSocket.bind(("", portNumber))

    def __del__(self):
        self.mbedSocket.close()

    # get next packet
    def getNextPacket(self):
        return self.mbedSocket.recvfrom(self.PACKET_BUFFER_SIZE)[0]




'''
socket: phone call btwn a computer or a device with another computer or server to communicate. 

TCP port number: specific endpoint in a server
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pre4e.org, 80))
                #host             #port number    destination to connect to
                #make a connection btwn this host at this por number. we havent sent any data yet

'''