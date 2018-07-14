import numpy as np
import random as ra
rooms = ["fw", "dr", "dl", "ur", "ul", "ud", "lr", "u", "d", "l", "r"]
rooms_top = ["dr", "dl","lr","d", "l", "r"]
rooms_bot = ["ur", "ul", "lr", "u", "l", "r"]
rooms_left = ["dr", "ur", "ud", "u", "d", "r", "ent"]
rooms_right = ["dl", "ul", "ud", "u", "d", "l", "ex"]
w, h = 9, 9; # make sure It's one more than the map size,
layout = [[0 for x in range(w)] for y in range(h)] # makes an array of zeros for height and width
test =  [[0 for x in range(w)] for y in range(h)]
for I in range(len(layout)):
    for H in range(len(layout[I])): # makes a random room for each coordinate
        if (H == 0 or H + 1 == w) and (I == 0  or I + 1 == h):
            layout[I][H] = "udlr"
        if (H == 1 or H == w) and (I == 1 or I == h):
            layout[I][H] = "q"
        elif I == 1:
            layout[I][H] = ra.choice(rooms_top)
        elif I == h:
            layout[I][H] = ra.choice(rooms_bot)
        elif H == 1:
            layout[I][H] = ra.choice(rooms_left)
        elif H == w:
            layout[I][H] = ra.choice(rooms_right)
        else:
            layout[I][H] = ra.choice(rooms)

