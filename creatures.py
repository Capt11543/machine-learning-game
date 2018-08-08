
class Hero:

    # FIXME: replace current_cors tuple with variables in the hero class
    # FIXME: maybe add a gear varaible? not sure how to handle that

    symbol = "☺"
    health = 100
    attack = 5
    defense = 10


class Goblin:

    symbol = "G"
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
