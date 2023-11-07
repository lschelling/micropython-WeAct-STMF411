import framebuf

class pbm:
    def __init__(self, pbmname):
        doc = open(pbmname,"rb")
        format=doc.readline()
        xy = doc.readline()
        self.x = int(xy.split()[0])
        self.y = int(xy.split()[1])
        icono = bytearray(doc.read())
        doc.close()
        self.framebuffer=framebuf.FrameBuffer(icono, self.x, self.y, framebuf.MONO_HLSB)
        
    def getSizeX(self):
        return self.x
    
    def getSizeY(self):
        return self.y
    
    def getFb(self):
        return self.framebuffer
