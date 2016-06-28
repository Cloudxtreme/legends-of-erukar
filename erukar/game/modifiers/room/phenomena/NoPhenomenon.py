from erukar.engine.model import Modifier
from erukar.engine.environment import Room
from erukar.game.modifiers.RoomModifier import RoomModifier

class NoPhenomenon(RoomModifier):
    Probability = 20
    def apply_to(self, room):
        pass
