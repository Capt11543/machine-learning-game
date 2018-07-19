import random as ra
import numpy as np

# game settings
width , height = 8,8
rooms = 0  # Room count
max_rooms = 32 # Max rooms allowed in the dude

max_rooms = int((width * height) / 2) # I think half is about the sweet spot, going lower tends to break it

# generates a 2d grid with diemensions (width, height
dungeon = np.zeros([width, height])

# things to help with computation
room_cors = [] # stores "marker rooms"
how_snakey = 69420 # decides where "marker rooms" will be

# chooses an entrance
dungeon[0][ra.randint(1, height - 1)] = 2

# bossin' it up baby
dungeon[width - 1][ra.randint(0, height - 1)] = 3

'''
the code below makes some "marker points"
these are randomly chosen points that basically fill space, and give the algorithm a starting point
they're picked by taking a random number in range (1 , width-1)
which randomly places it on a point every other row
'''

for x in range(1, width - 1):
    if x % 2 == 0:
        how_snakey = ra.randint(1, width - 1)
        dungeon[x][how_snakey] = 1
        room_cors.append([x, how_snakey])

'''
then we take those markers, and e x p a n d them up one
this makes it so they actually connect
we also extend the entrance and exit for the same reason
'''
for y in range(height):
    for x in range(width):
        if ([x,y]) in room_cors:
            dungeon[x - 1][y] = 1
        if dungeon[y][x] == 3:
            dungeon[y - 1][x] = 1
        if dungeon[y][x] == 2:
            dungeon[y + 1][x] = 1
'''
then we expand each room that's above a marker by one
'''
for y in range(height - 1):
    for x in range(width - 1):
        if dungeon[x][y] == 1 and not [x,y] in room_cors:
            dungeon[x][y + 1] = 1

'''
then, we splash in a couple random dudes so there's multiple paths to take, not all good ;)
'''
while rooms < max_rooms:
    for y in range(height - 1):
        for x in range(width - 1):
            rooms = np.count_nonzero(dungeon)
            if dungeon[x][y - 1] == 1 and dungeon[x][y] == 0:
                if ra.randint(0,10) > 7:
                    dungeon[x][y] = 1
            if dungeon[x - 1][y] == 1 and dungeon[x][y] == 0:
                if ra.randint(0,10) > 7:
                    dungeon[x][y] = 1
            if rooms >= max_rooms:
                break


if "n't" not in ra.choice(["rotate", "rotaten't"]): # randomly decides whether or not to rotate the map
    dungeon = np.rot90(dungeon)
rooms = np.count_nonzero(dungeon)
print(dungeon)
print(rooms)
print(max_rooms)