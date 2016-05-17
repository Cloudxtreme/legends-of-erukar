from pynarpg.model.EnvironmentPiece import EnvironmentPiece

class Room(EnvironmentPiece):
    North = 0
    East = 1
    South = 2
    West = 3

    def __init__(self):
        self.contents = []
        self.connections = [{} for x in range(0,4)]

    def connect_room(self, other_room, direction):
        pass

    def invert_direction(self, direction):
        return (direction + 2) % 4
