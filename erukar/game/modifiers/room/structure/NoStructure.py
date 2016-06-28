from erukar.engine.model import Modifier
from erukar.engine.environment import Room
from erukar.game.modifiers.RoomModifier import RoomModifier

class NoStructure(RoomModifier):
    Probability = 8
    def apply_to(self, room):
        pass
