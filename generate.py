
FILE = "fluff400.jpg"
OUTPUT = "fluff.txt"

# imports #

from progress_bar import progress
from PIL import Image

image = Image.open(FILE, 'r')

pixels = image.load()
width, height = image.size

print(f"Processing image of size ({width}, {height})")

# loop through pixels #

progress(0)
result = f"{width},{height},%PALETTE%,"

# how it will be formatted is:
# list of all colors
# then a list of pixels (auto wrapping on client end) as PALLETE INDEX, PIXEL COUNT (that is the specified color)
# [width, height, palette_count, (r, g, b), (r2, g2, b2), (etc), 0,1,1,6,0,65]

palette = []

# find all unique colors; this is very ineffecient using to loops but i cannot be bothered, feel free to optimize
# current 2*O(n) i think?
# it's slow on larger images, have fun :D
for x in range(width):
    progress(x / width * .5)
    for y in range(height):
        pixel = pixels[x, y]
        if pixel not in palette:
            palette.append(pixel)
            #print(pixel)
            result += f"{pixel},"
result = result.replace("%PALETTE%", str(len(palette)))

current_palette = None
current_palette_count = -1
for x in range(width):
    progress(x / width * .5 + .5)
    for y in range(height):
        pixel = pixels[x, y]
        color = palette.index(pixel) # get pallete index
        if current_palette != color: # if its a new color, submit the previous column info
            if current_palette != None:
                result += f"{current_palette},{current_palette_count},"
            current_palette = color # start more data for the [same] column
            current_palette_count = 1
        else:
            current_palette_count += 1 # otherwise, it's the same color so add to the count and keep going
result += f"{current_palette},{current_palette_count}" # add final row section because the loop won't capture it, obviously!

with open(OUTPUT, 'w') as f:
    f.write(result)
print("Done!") # limit of 5 characters, so it lines up with progress bar!