from erukar.game.modifiers.RoomModifier import RoomModifier
from erukar.engine.environment.Surface import Surface

class BeigeCarpetFloor(RoomModifier):
    Probability = 1.5

    def apply_to(self, room):
        room.floor = Surface('The floor of this room is a ragged beige color of carpet.')
