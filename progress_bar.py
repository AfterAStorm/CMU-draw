# imports #

from math import floor

# function #

def progress(i: float, seconds: float = -1):
    length = 30
    percent = str(round(i * 100))
    minutes = floor(seconds / 60)
    start = f" {(" " * (3 - len(percent)))}{percent}% [{"█" * round(i * length)}{"░" * round(length - (i * length))}] "
    if seconds > 0:
        print(f"{start}{minutes}m {seconds % 60:.2f}s    ", end="\r")
    else:
        print(start, end="\r")