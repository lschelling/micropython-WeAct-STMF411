import framebuf

def op_da(nom):
    doc = open(nom,"rb")
    doc.readline()
    xy = doc.readline()
    x = int(xy.split()[0])
    y = int(xy.split()[1])


    icono = bytearray(doc.read())
    doc.close()
    return(framebuf.FrameBuffer(icono, x, y, framebuf.MONO_HLSB))
