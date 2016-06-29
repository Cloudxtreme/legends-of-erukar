from erukar.engine.environment import Door, Surface

class Passage:
    def __init__(self, room=None, door=None):
        self.door = door
        self.room = room

    def is_not_empty(self):
        return self.door is not None and self.room is not None

    def on_inspect(self, relative_dir, inspect_walls):
        if self.door is not None:
            if type(self.door) is Surface and inspect_walls:
                return self.door.on_inspect(relative_dir.name)
            if type(self.door) is Door:
                return self.describe_door_in_direction(relative_dir.name)

        if self.room is not None:
            return self.room.inspect_peek(relative_dir.name)

        return None

    def describe_door_in_direction(self, direction):
        door_result = self.door.on_inspect(direction)
        if self.door.status == Door.Open:
            door_result += ' ' + self.room.inspect_peek(direction)
        return door_result
