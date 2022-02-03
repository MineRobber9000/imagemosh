import sys, traceback, random, struct, time, helpers
from os.path import splitext
from config import *

# helper functions
# converts an 8 bit color component into a component for luminance
def __componentfrom8bit(c):
    c = c/255
    if c<=0.03928:
        return c/12.92
    else:
        return ((c+0.055)/1.055)**2.4

# luminance and colorpack take colortuples, (r, g, b)
def luminance(ct):
    return 0.2126 * __componentfrom8bit(ct[0]) + 0.7152 * __componentfrom8bit(ct[1]) + 0.0722 * __componentfrom8bit(ct[2])

def colorpack(ct):
    return struct.pack("<4B",ct[2],ct[1],ct[0],0)

# output bytearray
out = bytearray(b'')

@helpers.errors_to_txt
def main(args):
    with open(args[1],"rb") as f:
        bmp_in = bytearray(f.read())

    # send the entire header into out
    out.extend(helpers.bmp_header(bmp_in))
    # now we can corrupt the palette
    # start by making a new palette
    newpalette = []
    for i in range(colors_used):
        newpalette.append((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    # now sort by reverse luminance (just as an attempt to match what I think Pillow might be doing with our BMP
    newpalette.sort(key=luminance,reverse=True)
    # now write the new palette into the bitmap
    for ct in newpalette:
        out.extend(colorpack(ct))
    out.extend(bmp_in[len(out):])
    # paste it into a file
    ts = int(time.time())
    with open(f"{ts}.bmp","wb") as f:
        f.write(out)

if __name__=="__main__": main(sys.argv)
