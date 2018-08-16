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

        if sugtype == "AttackThis":
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
    xpos = 300
    ypos = 300
    map_x = 0
    map_y = 0
    range = 200
    chasing = False
    id = None

    def __init__(self, enemies, layro):

        self.id = len(enemies)
        self.map_x = layro.map_x
        self.map_y = layro.map_y

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

    def behavior(self, gobbo, dude, game_win, layro):
        if self.map_x == layro.map_x and self.map_y == layro.map_y:
            if not self.chasing and dude in game_win.find_overlapping(self.xpos - self.range / 4,
                                                                      self.ypos - self.range / 4,
                                                                      self.xpos + self.range / 4,
                                                                      self.ypos + self.range / 4, ):
                # make the goblin angry if he sees layro
                game_win.itemconfig(gobbo, fill="red")
                self.chasing = True
                game_win.coords(gobbo, self.chase(layro.posx, layro.posy))

            # If the goblin is angry, he chases layro
            if self.chasing:
                game_win.coords(gobbo, self.chase(layro.posx, layro.posy))
                self.xpos, self.ypos = self.chase(layro.posx, layro.posy)
                if game_win.find_withtag("attack"):
                    game_win.coords("attack",
                                    game_win.coords(gobbo)[0] - 10,
                                    game_win.coords(gobbo)[1] - 10,
                                    game_win.coords(gobbo)[0] + 10,
                                    game_win.coords(gobbo)[1] + 10, )
                    global att_x, att_y
                    att_x = (game_win.coords("attack")[0] + game_win.coords("attack")[2]) / 2
                    att_y = (game_win.coords("attack")[1] + game_win.coords("attack")[3]) / 2

