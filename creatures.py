import random as ra


class Hero:

    # FIXME: maybe add a gear varaible? not sure how to handle that

    symbol = "☺"
    posx = 300
    posy = 300
    map_x = 0
    map_y = 0
    # These values should be treated as placeholders for now, and later we'll allow the player to create a character.
    health = 100
    attack = 5
    defense = 10

    def __init__(self, x, y):

        self.map_x = x
        self.map_y = y

    def rand_step(self):

        next_move = ra.choice(["up", "down", "left", "right", "nothing"])
        if next_move == "up":
            return self.posx, self.posy + 1
        if next_move == "down":
            return self.posx, self.posy - 1
        if next_move == "left":
            return self.posx - 1, self.posy
        if next_move == "right":
            return self.posx + 1, self.posy
        if next_move == "nothing":
            return self.posx, self.posy

    def sug_step(self, sugx, sugy, sugtype):

        up, down, left, right = False, False, False, False

        if sugtype == "MoveTo":
            if self.posx > sugx:
                left = True
            elif self.posx < sugx:
                right = True
            if self.posy > sugy:
                up = True
            elif self.posy < sugy:
                down = True

            if right and up:
                return self.posx + 1, self.posy - 1
            elif left and up:
                return self.posx - 1, self.posy - 1
            elif right and down:
                return self.posx + 1, self.posy + 1
            elif left and down:
                return self.posx - 1, self.posy + 1
            elif left:
                return self.posx - 1, self.posy
            elif right:
                return self.posx + 1, self.posy
            elif up:
                return self.posx, self.posy - 1
            elif down:
                return self.posx, self.posy + 1
            else:
                return self.posx, self.posy


class Goblin:

    symbol = "G"
    type = "Goblin"
    health = 100
    attack = 10
    defense = 5
    speed = .3
    xpos = 100
    ypos = 300
    range = 200
    chasing = False

    def chase(self, posx, posy):

        # increases speed, maybe too slowly?
        if self.speed < 2:
            self.speed += .001

        up, down, left, right = False, False, False, False

        # checks where layro is in reference to him, then returns coords to where he should move
        if posx < self.xpos:
            left = True
        elif posx > self.xpos:
            right = True
        if posy < self.ypos:
            up = True
        elif posy > self.ypos:
            down = True

        if right and up:
            return self.xpos + self.speed, self.ypos - self.speed
        elif left and up:
            return self.xpos - self.speed, self.ypos - self.speed
        elif right and down:
            return self.xpos + self.speed, self.ypos + self.speed
        elif left and down:
            return self.xpos - self.speed, self.ypos + self.speed
        elif left:
            return self.xpos - self.speed, self.ypos
        elif right:
            return self.xpos + self.speed, self.ypos
        elif up:
            return self.xpos, self.ypos - self.speed
        elif down:
            return self.xpos, self.ypos + self.speed
        else:
            return self.xpos, self.ypos
