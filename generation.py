import numpy as np
import random as rand

class Room:#Room class
    def __init__(self, top_door, bottom_door, left_door, right_door, is_entrance, is_boss):
        #All of these should be bools
        self.top_door = top_door
        self.bottom_door = bottom_door
        self.left_door = left_door
        self.right_door = right_door
        self.is_entrance = is_entrance
        self.is_boss = is_boss

#We'll use these to make sure that only one entrance and boss room are made
has_entrance = False
has_boss = False

#Setup map
width, height = 9, 9#Must be one more than the actual map of the
dungeon_map = [[0 for x in range(width)] for y in range(height)]#Multidimensional list for map
rooms = 0#Room count

#First, generate an entrance room
while not has_entrance:#Make sure this creates an entrance
    for index in range(len(dungeon_map[0])):#Limited to the top row for now because I'm too lazy to figure out how to make it on the sides lol
        if rand.randint(1, width) == width:#Should be a 1 in width chance
            dungeon_map[0][index] = Room(True, rand.choice([True, False]), rand.choice([True, False]), rand.choice([True, False]), True, False)#Generate a room with a top door (entrance), and randomly give it a left, right, and/or bottom door
            has_entrance = True#Show in program that entrance has been created
            rooms += 1#Update room count
            break#Instantly exit the loop for good measure

#Next, generate all the other necessary rooms
while not has_boss:#Run as long as there is no boss
    for index_y in range(len(dungeon_map)):#Y loop
        for index_x in range(len(dungeon_map[index_y])):#X loop
            if rooms >= 8:#This will make it so that the boss is only generated after 8 rooms
                if dungeon_map[index_y][index_x] == 0:#If the map index is empty...
                    # Determine whether the room will be a boss room
                    if rand.randint(1, 8) == 8:
                        boss_room = True
                    else:
                        boss_room = False

                    if boss_room:#If the room will be a boss room...
                        if not dungeon_map[index_y - 1][index_x] == 0 and not dungeon_map[index_y][index_x - 1] == 0:#If there is a room above and to the left of the current map index...
                            dungeon_map[index_y][index_x] = Room(True, rand.choice([True, False]), True, rand.choice([True, False]), False, True)#Generate a boss room that has a top door and a left door, and randomly give it a right and/or bottom door
                            rooms += 1#Update room count
                            has_boss = True#Dungeon has boss room now
                            break#Exit loop for good measure
                        elif not dungeon_map[index_y - 1][index_x] == 0:#If not, but if there is a room above the current map index...
                            dungeon_map[index_y][index_x] = Room(True, rand.choice([True, False]), False, rand.choice([True, False]), False, True)#Generate a boss room that has a top door, randomly give it a right and/or bottom door, and do not give it a left door
                            rooms += 1#Update room count
                            has_boss = True#Dungeon has boss room now
                            break#Exit loop for good measure
                        elif not dungeon_map[index_y][index_x - 1] == 0:#If not, but if there is a room to the left of the current map index...
                            dungeon_map[index_y][index_x - 1] = Room(False, rand.choice([True, False]), True, rand.choice([True, False]), False, True)#Generate a boss room that has a left door, randomly give it a right and/or bottom door, and do not give it a top door
                            rooms += 1#Update room count
                            has_boss = True#Dungeon has boss room now
                            break#Exit loop for good measure
                    else:
                        if not dungeon_map[index_y - 1][index_x] == 0 and not dungeon_map[index_y][index_x - 1] == 0:#If there is a room above and to the left of the current map index...
                            dungeon_map[index_y][index_x] = Room(True, rand.choice([True, False]), True, rand.choice([True, False]), False, False)#Generate a room that has a top door and a left door, and randomly give it a right and/or bottom door
                            rooms += 1#Update room count
                        elif not dungeon_map[index_y - 1][index_x] == 0:#If not, but if there is a room above the current map index...
                            dungeon_map[index_y][index_x] = Room(True, rand.choice([True, False]), False, rand.choice([True, False]), False, False)#Generate a room that has a top door, randomly give it a right and/or bottom door, and do not give it a left door
                            rooms += 1#Update room count
                        elif not dungeon_map[index_y][index_x - 1] == 0:  # If not, but if there is a room to the left of the current map index...
                            dungeon_map[index_y][index_x - 1] = Room(False, rand.choice([True, False]), True, rand.choice([True, False]), False, False)#Generate a room that has a left door, randomly give it a right and/or bottom door, and do not give it a top door
                            rooms += 1#Update room count
            else:#Copy-paste of above code, except rooms are guaranteed to not be boss rooms
                if dungeon_map[index_y][index_x] == 0:#If the map index is empty...
                    if not dungeon_map[index_y - 1][index_x] == 0 and not dungeon_map[index_y][index_x - 1] == 0:#If there is a room above and to the left of the current map index...
                        dungeon_map[index_y][index_x] = Room(True, rand.choice([True, False]), True, rand.choice([True, False]), False, False)#Generate a room that has a top door and a left door, and randomly give it a right and/or bottom door
                        rooms += 1#Update room count
                    elif not dungeon_map[index_y - 1][index_x] == 0:#If not, but if there is a room above the current map index...
                        dungeon_map[index_y][index_x] = Room(True, rand.choice([True, False]), False, rand.choice([True, False]), False, False)#Generate a room that has a top door, randomly give it a right and/or bottom door, and do not give it a left door
                        rooms += 1#Update room count
                    elif not dungeon_map[index_y][index_x - 1] == 0:#If not, but if there is a room to the left of the current map index...
                        dungeon_map[index_y][index_x - 1] = Room(False, rand.choice([True, False]), True, rand.choice([True, False]), False, False)#Generate a room that has a left door, randomly give it a right and/or bottom door, and do not give it a top door
                        rooms += 1#Update room count

#Next, print it
for index_y in range(len(dungeon_map)):#Y loop
    for index_x in range(len(dungeon_map[index_y])):#X loop
        if not dungeon_map[index_y][index_x] == 0:#Check that there is a room stored here (is this necessary?)
            if dungeon_map[index_y][index_x].is_entrance:
                print('E', end='')#Print E if it's the entrance
            elif dungeon_map[index_y][index_x].is_boss:
                print('B', end='')#Print B if it's the boss
            else:
                print('X', end='')#Print X if it's just a normal room
        else:
            print(' ', end='')#Print a space if there's no room there
    
    print("\n")#Print a new line (hopefully it will look like a grid)