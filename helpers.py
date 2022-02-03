import struct
# constants for peeking around in the file
FILE_START = 0x0000
BITMAP_PTR = 0x000a
HEADER_SIZE = 0x000e
BPP = 0x001c
COMPRESSION = 0x001e
PALETTE_BEGINS = 0x0036

def value(array,index,formatstr="I"):
    formatstr = "<"+formatstr # bitmaps should be little-endian
    size = struct.calcsize(formatstr)
    return struct.unpack(formatstr,array[index:index+size])[0]

def bmp_header(bmp_in):
    assert value(bmp_in,FILE_START,"2s")==b'BM',"Invalid bitmap file"
    assert value(bmp_in,HEADER_SIZE)==40, "I don't know how to read this header"
    assert value(bmp_in,BPP,"H")<=8,"Non-paletted bitmap file"
    assert value(bmp_in,COMPRESSION)<=2,"Non-RLE compression (not sure if we can do it)" # 0=no compression, 1=RLE8, 2=RLE4. otherwise we're likely not having a lot of fun today
    return bmp_in[:PALETTE_BEGINS] # return header

def start_bitmap_data(bmp_in):
    return value(bmp_in,BITMAP_PTR)

from functools import wraps
import traceback

def errors_to_txt(func):
    @wraps(func)
    def __wrapper(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except:
            with open("error.txt","w") as f:
                traceback.print_exc(file=f)
    return __wrapper
