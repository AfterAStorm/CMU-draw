
FILE = "out.txt"
WAIT_TIME = .02
CHARACTERS_PER_TICK = 5

# imports #

from pynput.keyboard import Controller
from progress_bar import progress
from time import sleep

with open(FILE, 'r') as f:
    data = f.read()

# countdown #

# print without going to next line
def printr(*any):
    print(*any, end='\r')

# 3, 2, 1
for i in range(3, 0, -1):
    printr(i)
    sleep(1)

# script

keyboard = Controller()

# split data to where with CHARACTERS_PER_TICK as 5, it will be "abcdefghijkl" to ["abced", "efghi", "jklmn"]
split = [data[i:i + CHARACTERS_PER_TICK] for i in range(0, len(data), CHARACTERS_PER_TICK)]
splits = len(split)

for i in range(splits):
    text = split[i]
    secondsLeft = (WAIT_TIME * splits) - (splits * WAIT_TIME * (i / splits))
    progress(i / splits, secondsLeft)
    keyboard.type(text)
    sleep(WAIT_TIME)
    
print("Done!")