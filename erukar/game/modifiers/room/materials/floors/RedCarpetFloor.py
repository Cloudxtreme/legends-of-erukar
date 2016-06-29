from erukar.game.modifiers.RoomModifier import RoomModifier
from erukar.engine.environment.Surface import Surface

class RedCarpetFloor(RoomModifier):
    Probability = 1.5

    def apply_to(self, room):
        room.floor = Surface('The floor of this room is a soft red carpet.')
