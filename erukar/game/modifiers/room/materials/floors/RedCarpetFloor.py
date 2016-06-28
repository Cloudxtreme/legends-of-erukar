from erukar.engine.model import Modifier
from erukar.engine.environment import Room
from erukar.game.modifiers.RoomModifier import RoomModifier

class RedCarpetFloor(RoomModifier):
    Probability = 1.5

    def apply_to(self, room):
        room.description += 'The floor of this room is a soft red carpet. '
