from erukar.game.modifiers.RoomModifier import RoomModifier
from erukar.engine.environment.Surface import Surface

class StoneFloor(RoomModifier):
    Probability = 3

    def apply_to(self, room):
        room.floor = Surface('This room has a flat stone floor.')
