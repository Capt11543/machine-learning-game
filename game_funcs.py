from generator import dungeon as map


def room_walls(xcor, ycor):
    top = True
    bot = True
    left = True
    right = True

    try:
        if map[xcor][ycor - 1] == 0 or ycor == 0:
            left = False
    except IndexError:
        left = False
    try:
        if map[xcor][ycor + 1] == 0:
            right = False
    except IndexError:
        right = False
    try:
        if map[xcor + 1][ycor] == 0:
            bot = False
    except IndexError:
        bot = False
    try:
        if map[xcor - 1][ycor] == 0 or xcor == 0:
            top = False
    except IndexError:
        top = False

    return left, right, bot, top
