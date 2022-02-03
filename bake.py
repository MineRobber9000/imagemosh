from PIL import Image
import sys, helpers

@helpers.errors_to_txt
def main(args):
    # bake image
    im = Image.open(args[1])
    im.save(args[1]+".png")

if __name__=="__main__": main(sys.argv)
