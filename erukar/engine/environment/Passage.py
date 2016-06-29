class Passage:
    def __init__(self, room=None, door=None):
        self.door = door
        self.room = room

    def is_not_empty(self):
        return self.door is not None and self.room is not None
