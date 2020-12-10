from abc import ABC, abstractmethod

class FirmwareChannel(ABC):

    @abstractmethod
    def getNextPacket(self):
        pass


