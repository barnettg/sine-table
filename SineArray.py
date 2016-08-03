# generates sine table array for one period
#   for an 8-bit DAC, selecting the size of the array
# prints a C array of uint8
# prints variable with array size

import math
class SineData:
    
    def __init__(self, totalSamples, numberOfBits):
        self.btArray = []
        self.btArrayLength = totalSamples
        self.bits = numberOfBits
        self.maxVal = math.pow(2,numberOfBits)-1
        self.halfMax = self.maxVal / 2.0
        print(self.maxVal)
        print(self.halfMax)


    def getSinedata(self):
        # sine (2*pi* sample/(total samples) )
        reply = True
        for Sample in range(self.btArrayLength):
            val = math.sin(2*math.pi* (Sample/self.btArrayLength))
            val = int(127.5 * val)
            val = val + 127
            self.btArray.append(val)
        print(self.btArray)
        return reply

    
    def writeData(self):
        reply = True
        outfilename=input("Enter the output file name: ")
        arrayname = input("Enter the array name name: ")
        outF = None
        try:
            outF = open(outfilename, 'w')
            varname = "uint16 " + arrayname+"Size = " + str(self.btArrayLength) + ";\n"
            outF.write(varname)
            outF.write("volatile const uint8 %s[ ] = {\n" % arrayname)

            line = 0
            for byte in self.btArray:
                #print ("%d, " % byte, end = '')
                outF.write("%3d, " % byte)
                line = line +1
                if line>15:
                    #print ("")
                    outF.write("\n")
                    line = 0
            outF.write("0 };\n")
        except:
            reply = False
        finally:
            if outF != None:
                outF.close()
        
        return reply
    
        
    def start(self):
        self.getSinedata()
        self.writeData()
        print ("Done")


if __name__ == "__main__":
    sz = input("Enter number of sine points per cycle: ")
    bits = input("Enter number of bits: ")
    sd = SineData(int(sz),int(bits))
    #sd.start()


