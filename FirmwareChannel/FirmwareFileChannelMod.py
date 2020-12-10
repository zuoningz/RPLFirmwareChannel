from FirmwareChannel import FirmwareChannel as FC
import asn1tools
import base64
import os


'''DAQMessages.asn and ProgrammingTypes.asn need to be same directory as the running/testing file'''
#print("in FFC File")
class FirmwareFileChannel(FC.FirmwareChannel):
    def __init__(self,file):
        #print("in FirmwareFileC constructor")
        self.file = file
        self.counter = 0
        self.f = open(self.file,'r')
        self.dataList = list()
        asn1_dir = os.path.join("")#("../../../../Downloads", "..")
        self.daq_messages = asn1tools.compile_files(
            [os.path.join(asn1_dir, "DAQMessages.asn"),
            os.path.join(asn1_dir, "ProgrammingTypes.asn")],
            codec="oer")

    def getNextPacket(self):

    
        line = self.f.readline() #self.f[self.counter]
        line = line[0: -1]
        lineBytes = base64.b64decode(line)
        data = self.daq_messages.decode("DataMessageList", lineBytes)
        self.dataList.extend(data)
       # self.counter += 1
        return data

    def __del__(self):
        self.f.close()