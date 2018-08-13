class Room:
    # Define variables
    x_pos = None
    y_pos = None
    room_type = None
    # type=0 for no room, type=1 for normal room, type=2 for entrance room, type=3 for boss

    discovered = False

    def __init__(self, x_pos, y_pos, room_type):  # Takes parameters for X and Y coordinates, and type
        # Set coordinates equal to parameters
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.room_type = room_type  # Room type

    def set_discovered(self, discovered):  # Change whether or not the room has been discovered
        self.discovered = discovered