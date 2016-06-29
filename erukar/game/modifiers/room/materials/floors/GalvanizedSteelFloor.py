from erukar.game.modifiers.RoomModifier import RoomModifier
from erukar.engine.environment.Surface import Surface

class GalvanizedSteelFloor(RoomModifier):
    Probability = 0.1

    def apply_to(self, room):
        room.floor = Surface('The floor seems to be made of a galvanized steel with tread patterns.')
