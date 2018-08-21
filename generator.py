import random as ra
import numpy as np
from creatures import Hero
from room import Room

width, height = 8, 8

# game settings
rooms = 0  # Room count
counter_dude = 0

max_rooms = int((width * height) / 2)  # I think half is about the sweet spot, going lower tends to break it

# generates a 2d grid with dimensions (width, height)
dungeon = np.zeros([width, height])

# things to help with computation
room_cors = []  # stores "marker rooms"

# chooses an entrance
dungeon[0, ra.randint(1, height - 1)] = 2

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
        dungeon[x][how_snakey] = 1  # Room(x, how_snakey, 1)
        room_cors.append([x, how_snakey])

'''
then we take those markers, and e x p a n d them up one
this makes it so they actually connect
we also extend the entrance and exit for the same reason
'''
for y in range(height):
    for x in range(width):
        if ([x, y]) in room_cors:
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
        if dungeon[x][y] == 1 and not [x, y] in room_cors:
            dungeon[x][y + 1] = 1

'''
then, we splash in a couple random dudes so there's multiple paths to take, not all good ;)
'''
while rooms < max_rooms and counter_dude < 10:
    counter_dude += 1
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            rooms = np.count_nonzero(dungeon)
            if dungeon[x][y - 1] == 1 and dungeon[x][y] == 0:
                if ra.randrange(0, 10) > 4:
                    dungeon[x][y] = 1
            if dungeon[x - 1][y] == 1 and dungeon[x][y] == 0:
                if ra.randrange(0, 10) > 4:
                    dungeon[x][y] = 1
            if rooms >= max_rooms:
                break

if "n't" not in ra.choice(["rotate", "rotaten't"]):  # randomly decides whether or not to rotate the map
    dungeon = np.rot90(dungeon)

dungeon_map = []
for ypos in range(len(dungeon)):
    map_row = []
    for xpos in range(len(dungeon[ypos])):
        map_row.append(Room(xpos, ypos, dungeon[xpos][ypos]))
    dungeon_map.append(map_row)

for x in range(len(dungeon)):
    for y in range(len(dungeon[x])):
        if dungeon_map[x][y].room_type == 2:
            layro = Hero(y, x)


def regenerate(w, h):

    global max_rooms, dungeon, room_cors, how_snakey, counter_dude, rooms, dungeon_map, map_row, layro
    width, height = w, h
    max_rooms = int((w * h) / 2)  # I think half is about the sweet spot, going lower tends to break it

    # generates a 2d grid with dimensions (width, height)
    dungeon = []
    dungeon_map = []
    dungeon = np.zeros([width, height])

    # things to help with computation
    room_cors = []  # stores "marker rooms"

    # chooses an entrance
    dungeon[0, ra.randint(1, height - 1)] = 2

    # bossin' it up baby
    dungeon[width - 1][ra.randint(0, height - 1)] = 3

    for xpos in range(1, width - 1):
        if xpos % 2 == 0:
            how_snakey = ra.randint(1, width - 1)
            dungeon[xpos][how_snakey] = 1
            room_cors.append([xpos, how_snakey])

    for ypos in range(height):
        for xpos in range(width):
            if ([xpos, ypos]) in room_cors:
                dungeon[xpos - 1][ypos] = 1
            if dungeon[ypos][xpos] == 3:
                dungeon[ypos - 1][xpos] = 1
            if dungeon[ypos][xpos] == 2:
                dungeon[ypos + 1][xpos] = 1

    for ypos in range(height - 1):
        for xpos in range(width - 1):
            if dungeon[xpos][ypos] == 1 and not [xpos, ypos] in room_cors:
                dungeon[xpos][ypos + 1] = 1

    while rooms < max_rooms and counter_dude < 10:
        counter_dude += 1
        for ypos in range(1, height - 1):
            for xpos in range(1, width - 1):
                rooms = np.count_nonzero(dungeon)
                if dungeon[xpos][ypos - 1] == 1 and dungeon[xpos][ypos] == 0:
                    if ra.randrange(0, 10) > 4:
                        dungeon[xpos][ypos] = 1
                if dungeon[xpos - 1][ypos] == 1 and dungeon[xpos][ypos] == 0:
                    if ra.randrange(0, 10) > 4:
                        dungeon[xpos][ypos] = 1
                if rooms >= max_rooms:
                    break

    dungeon_map = []
    for ypos in range(len(dungeon)):
        map_row = []
        for xpos in range(len(dungeon[ypos])):
            map_row.append(Room(xpos, ypos, dungeon[xpos][ypos]))
        dungeon_map.append(map_row)

    for y in range(len(dungeon)):
        for x in range(len(dungeon[y])):
            if dungeon_map[x][y].room_type == 2:
                layro.map_x, layro.map_y = x, y
