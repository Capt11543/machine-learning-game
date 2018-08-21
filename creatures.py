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
    equipped_weapon = "nothing"
    equipped_armor = "nothing"
    equipped_access = "nothing"
    # can be one_square, surrounding, or range
    attack_type = "one_square"

    def __init__(self, x, y, *args):

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
    color = "light green"
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


class Shade:
    symbol = "S"
    type = "Shade"
    color = "#c47266"
    health = 20
    attack = 0
    defense = 5
    speed = 2
    xpos = 100
    ypos = 300
    map_x = 0
    map_y = 0
    timer = 0
    projectile = False
    proj_x = 100
    proj_y = 300
    target_x = 0
    target_y = 0
    visible = False
    id = None
    proj = None
    speed = 6.5

    def __init__(self, enemies, layro):
        self.id = len(enemies)
        self.map_x = layro.map_x
        self.map_y = layro.map_y
        self.visible = True

    def proj_move(self, dude, game_win, layro):

        if self.target_x + self.speed > self.proj_x > self.target_x - self.speed and self.target_y + self.speed > self.proj_y > self.target_y - self.speed:
            self.projectile = False
            game_win.delete(proj)

        else:
            up, down, left, right = False, False, False, False

            if self.target_x < self.proj_x:
                left = True
            elif self.target_x > self.proj_x:
                right = True
            if self.target_y < self.proj_y:
                up = True
            elif self.target_y > self.proj_y:
                down = True

            if right and up:
                self.proj_x, self.proj_y = self.proj_x + self.speed, self.proj_y - self.speed
            elif left and up:
                self.proj_x, self.proj_y = self.proj_x - self.speed, self.proj_y - self.speed
            elif right and down:
                self.proj_x, self.proj_y = self.proj_x + self.speed, self.proj_y + self.speed
            elif left and down:
                self.proj_x, self.proj_y = self.proj_x - self.speed, self.proj_y + self.speed
            elif left:
                self.proj_x, self.proj_y = self.proj_x - self.speed, self.proj_y
            elif right:
                self.proj_x, self.proj_y = self.proj_x + self.speed, self.proj_y
            elif up:
                self.proj_x, self.proj_y = self.proj_x, self.proj_y - self.speed
            elif down:
                self.proj_x, self.proj_y = self.proj_x, self.proj_y + self.speed
            else:
                self.proj_x, self.proj_y = self.proj_x, self.proj_y

    def behavior(self, ghost, dude, game_win, layro):
        self.timer += 1
        if self.timer == 150:
            game_win.itemconfig(ghost, fill="black")
            self.visible = False

        if self.timer == 160:
            global proj
            proj = game_win.create_text(self.xpos, self.ypos, text="O",
                                        fill="#c47266", tags=("shade-projectile","room-specific"), font=("times", 10))
            self.target_x = game_win.coords(dude)[0]
            self.target_y = game_win.coords(dude)[1]
            self.projectile = True

        if self.projectile:
            self.proj_move(dude, game_win, layro)
            game_win.coords(proj, self.proj_x, self.proj_y)
        else:
            self.proj_x, self.proj_y = self.xpos, self.ypos

        if self.timer == 250:
            game_win.itemconfig(ghost, fill="#c47266")
            self.xpos, self.ypos = ra.randint(50, 340), ra.randint(50, 450)
            game_win.coords(ghost, self.xpos, self.ypos)
            self.timer = 0
            self.visible = True




