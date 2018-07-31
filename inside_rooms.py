from generator_working import *


def room_walls(x, y):
    top = False
    bot = False
    left = False
    right = False

    try:
        if dungeon[x][y - 1] != 0:
            left = True
    finally:
        try:
            if dungeon[x][y + 1] != 0:
                right = True
        finally:
            try:
                if dungeon[x - 1][y] != 0:
                    bot = True
            finally:
                try:
                    if dungeon[x + 1][y] != 0:
                        top = True
                finally:
                    return left, right, bot, top



