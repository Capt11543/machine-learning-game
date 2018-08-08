import random as ra
from generator_working import dungeon


# FIXME: should these top two be a member of the Hero class?
def rand_step(posx, posy, scale):
    next_move = ra.choice(["up", "down", "left", "right", "nothing"])
    if next_move == "up":
        return posx, posy + scale
    if next_move == "down":
        return posx, posy - scale
    if next_move == "left":
        return posx - scale, posy
    if next_move == "right":
        return posx + scale, posy
    if next_move == "nothing":
        return posx, posy


def sug_step(posx, posy, sugx, sugy, sugtype, scale):

    up, down, left, right = False, False, False, False

    if sugtype == "MoveTo":
        if posx > sugx:
            left = True
        elif posx < sugx:
            right = True
        if posy > sugy:
            up = True
        elif posy < sugy:
            down = True

        if right and up:
            return posx + scale, posy - scale
        elif left and up:
            return posx - scale, posy - scale
        elif right and down:
            return posx + scale, posy + scale
        elif left and down:
            return posx - scale, posy + scale
        elif left:
            return posx - scale, posy
        elif right:
            return posx + scale, posy
        elif up:
            return posx, posy - scale
        elif down:
            return posx, posy + scale
        else:
            return posx, posy


# FIXME: This is probably where to look to fix the ghost left door

def room_walls(xcor, ycor):
    top = True
    bot = True
    left = True
    right = True

    try:
        if dungeon[xcor][ycor - 1] == 0:
            left = False
    except IndexError:
        left = False
    try:
        if dungeon[xcor][ycor + 1] == 0:
            right = False
    except IndexError:
        right = False
    try:
        if dungeon[xcor + 1][ycor] == 0:
            bot = False
    except IndexError:
        bot = False
    try:
        if dungeon[xcor - 1][ycor] == 0:
            top = False
    except IndexError:
        top = False

    return left, right, bot, top
