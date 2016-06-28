from erukar.engine.model import Modifier
from erukar.engine.environment import Room
from erukar.game.modifiers.RoomModifier import RoomModifier

class DimLight(RoomModifier):
    Probability = 1
    def apply_to(self, room):
        room.description += 'The features of this room are dulled by dim lighting. '
