from cmu_graphics import * # type: ignore | the type ignore makes VSC's PyLance SHUT!

# put data in-between brackets
pixels = []

# code
from math import floor, ceil
from time import time

palette = []

def progress(i: float, seconds: float = -1):
    length = 30
    percent = str(rounded(i * 100))
    minutes = floor(seconds / 60)
    start = f" {(" " * (3 - len(percent)))}{percent}% [{"█" * rounded(i * length)}{"░" * rounded(length - (i * length))}] "
    if seconds > 0:
        print(f"{start}{minutes}m {seconds % 60:.2f}s    ", end="\r")
    else:
        print(start, end="\r")

# get width/height
width = pixels.pop(0)
height = pixels.pop(0)
colors = pixels.pop(0)

start = time()
print("Getting colors...")
for i in range(colors):
    timeProgressed = time() - start
    percent = i / colors + .0001
    timeRemaining = timeProgressed * (1 / (percent) - 1)
    progress(percent, timeRemaining)
    color = pixels.pop(0)
    palette.append(rgb(color[0], color[1], color[2]))
print()
area = width * height

# loop
app.setMaxShapeCount(width * height)
app.pixel_counter = 0

# rounded because it's cmu's python round, aparently "round" doesn't do what you would expect?
offsetx = rounded(1 / width  * 400) # scale with image size; ex: image 400 is (1/400*400) is 1, so 1 pixel on the image is 1 pixel  on the canvas
offsety = rounded(1 / height * 400) #                        ex: image 200 is (1/200*400) is 2, so 1 pixel on the image is 2 pixels on the canvas

def clamp(a, mi, ma):
    return max(mi, min(a, ma))

def draw_pixels(color_index, count):
    color = palette[color_index]
    
    for i in range(count):
        x = floor(app.pixel_counter / height)
        y = app.pixel_counter % height
        app.pixel_counter += 1
        Rect(x * offsetx, y * offsety, clamp(ceil(offsetx), 1, 99999999999999), clamp(ceil(offsety), 1, 999999999), fill=color)
    
    #print(x, y, "         ", end='\r')
    #Rect(rounded(x * offsetx), rounded(y * offsety), offsetx, rounded(offsety * count), fill=color) # impliactions, would be better but i'd have to modify the generate.py to start new thing on new column

start = time()
print("Printing pixels...")
for i in range(0, len(pixels), 2):
    timeProgressed = time() - start
    percent = i / len(pixels) + .0001
    timeRemaining = timeProgressed * (1 / (percent) - 1)
    progress(percent, timeRemaining)
    color = pixels[i]#x * width + x * 2 + y    ]
    count = pixels[i + 1]#x * width + x * 2 + y + 1]
    
    draw_pixels(color, count)
print()

#print(palette)
cmu_graphics.run() # type: ignore
