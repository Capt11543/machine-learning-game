import random as ra


class Room:
    # Define variables
    x_pos = None
    y_pos = None
    room_type = None
    contents = []

    # type=0 for no room, type=1 for normal room, type=2 for entrance room, type=3 for boss

    discovered = False

    def __init__(self, y_pos, x_pos, room_type):  # Takes parameters for X and Y coordinates, and type

        temp_contents = []

        # Set coordinates equal to parameters
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.room_type = room_type  # Room type

        if room_type == 1:
            if ra.randint(0, 5) == 4:
                temp_contents.append("gob_pos1")

        self.contents = temp_contents

    def set_discovered(self, discovered):  # Change whether or not the room has been discovered
        self.discovered = discovered
