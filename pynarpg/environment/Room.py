from pynarpg.model.EnvironmentPiece import EnvironmentPiece

class Room(EnvironmentPiece):
    North = 1
    East = 2
    South = 3
    West = 4
    
    def __init__(self):
        self.contents = []
        self.connections = {}

    def connect_room(self, other_room, direction):
        pass
