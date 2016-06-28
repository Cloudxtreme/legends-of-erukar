from erukar.engine.model import Modifier
from erukar.engine.environment import Room
from erukar.game.modifiers.RoomModifier import RoomModifier

class MudFloor(RoomModifier):
    Probability = 1

    def apply_to(self, room):
        room.description += 'The floor of this room is dirt, but some sort moisture has turned it into a thick, viscous mud. '
