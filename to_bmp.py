from PIL import Image
import sys, traceback, os.path, helpers
from config import *

def crop_image_to(im,w,h):
    if w is None or h is None: return im
    imw, imh = im.size
    # get desired aspect ratio
    # if imw<imh: # gotta crop height
    #     desw = int(imh*(w/h))
    #     wmargin = int((imw/2)-(desw/2))
    #     im = im.crop((wmargin,0,imw-wmargin,imh))
    # else: # gotta crop width
    desh = int(imw*(h/w))
    hmargin = int((imh/2)-(desh/2))
    im = im.crop((0,hmargin,imw,imh-hmargin))
    return im.resize((w,h))

@helpers.errors_to_txt
def main(args):
    # open image
    im = Image.open(args[1])
    # quantize to 16 colors (turn off dither pattern insofar as we can)
    im = crop_image_to(im,DESIRED_WIDTH,DESIRED_HEIGHT).quantize(colors_used,dither=Image.NONE)
    # save as bmp
    im.save(os.path.splitext(args[1])[0]+".bmp")

if __name__=="__main__": main(sys.argv)
