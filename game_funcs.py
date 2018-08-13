from generator import dungeon_map as map

def room_walls(xcor, ycor):
    top = True
    bot = True
    left = True
    right = True

    try:
        if map[xcor][ycor - 1].room_type == 0:
            left = False
    except IndexError:
        left = False
    try:
        if map[xcor][ycor + 1].room_type == 0:
            right = False
    except IndexError:
        right = False
    try:
        if map[xcor + 1][ycor].room_type == 0:
            bot = False
    except IndexError:
        bot = False
    try:
        if map[xcor - 1][ycor].room_type == 0:
            top = False
    except IndexError:
        top = False

    return left, right, bot, top