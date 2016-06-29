from erukar.game.modifiers.RoomModifier import RoomModifier
from erukar.engine.environment.Surface import Surface

class MudFloor(RoomModifier):
    Probability = 1

    def apply_to(self, room):
        room.floor = Surface('The floor of this room is dirt, but some sort moisture has turned it into a thick, viscous mud.')
