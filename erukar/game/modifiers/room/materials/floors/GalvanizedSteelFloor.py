from erukar.engine.model import Modifier
from erukar.engine.environment import Room
from erukar.game.modifiers.RoomModifier import RoomModifier

class GalvanizedSteelFloor(RoomModifier):
    Probability = 0.1

    def apply_to(self, room):
        room.description += 'The floor seems to be made of a galvanized steel with tread patterns. '
