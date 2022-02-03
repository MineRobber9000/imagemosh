# imagemosh

A set of Python scripts for messing with bitmaps. Requires PIL/Pillow.

## So what does each script do?

I'm glad you asked.

 - `config.py` - Not actually a script, contains the parameters for the other scripts to do their things.
    - `DESIRED_WIDTH`/`DESIRED_HEIGHT` - Crops the bitmap to the desired width and height (in `to_bmp.py`). Set either to `None` to disable the conversion.
    - `colors_used` - Sets the number of colors in the bitmap. (PIL/Pillow will export it as a 256-color bitmap, but we can affect how many of those 256 colors we actually use.)
 - `helpers.py` - Also not actually a script, contains helper functions for messing with BMP and writing scripts.
 - `to_bmp.py` - Converts any image readable by PIL/Pillow to an indexed bitmap, for use with the other scripts.
 - `fuzz_palette.py` - Generates a random palette and writes it over the palette in the image (changing all of the colors).
 - `blender.py` - Swaps 2 bitmaps' entire palettes. Useful for testing certain color/photo combinations without needing a way to seed the RNG.
 - `bake.py` - Converts the bitmap into a PNG file, suitable for sharing on modern social media platforms.

All scripts are drag-and-drop on Windows, except for `blender.py` which takes 2 bitmaps (if you drag-and-drop 2 bitmaps onto it, it'll work, if you drag 1 bitmap onto it it'll ask you for the other, and if you just click on it, it'll ask you for both).
