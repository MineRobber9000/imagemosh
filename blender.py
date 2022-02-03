import sys, helpers, os.path
import tkinter, tkinter.filedialog

root = tkinter.Tk()
root.withdraw()

@helpers.errors_to_txt
def main(args):
    im1, im2 = None, None
    if len(args)==3:
        _, im1, im2 = args
    elif len(args)==2:
        _, im1 = args
    if im1 is None: im1 = tkinter.filedialog.askopenfilename(title="Select first bitmap",filetypes=[("Bitmap images","*.bmp")])
    if im1 and im2 is None: im2 = tkinter.filedialog.askopenfilename(title="Select second bitmap",filetypes=[("Bitmap images","*.bmp")])
    if not (im1 and im2): return # cancelled
    with open(im1,"rb") as f:
        im1d = bytearray(f.read())
    with open(im2,"rb") as f:
        im2d = bytearray(f.read())

    im1o = bytearray()
    im2o = bytearray()

    # each one keeps their header
    im1o.extend(helpers.bmp_header(im1d))
    im2o.extend(helpers.bmp_header(im2d))

    # now take the palette data from each and put it into the other
    im1o.extend(im2d[helpers.PALETTE_BEGINS:helpers.start_bitmap_data(im2d)])
    im2o.extend(im1d[helpers.PALETTE_BEGINS:helpers.start_bitmap_data(im1d)])

    # now paste the rest of the file in there
    im1o.extend(im1d[len(im1o):])
    im2o.extend(im2d[len(im2o):])

    # and now save
    with open(os.path.splitext(os.path.basename(im1))[0]+"_flipped.bmp","wb") as f:
        f.write(im1o)

    with open(os.path.splitext(os.path.basename(im2))[0]+"_flipped.bmp","wb") as f:
        f.write(im2o)

if __name__=="__main__":
    main(sys.argv)
#    root.close()
