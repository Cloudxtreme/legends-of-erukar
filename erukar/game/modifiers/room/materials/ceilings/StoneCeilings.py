from erukar.engine.model import Modifier
from erukar.engine.environment import Room
from erukar.game.modifiers.RoomModifier import RoomModifier

class StoneCeilings(RoomModifier):
    Probability = 3

    def apply_to(self, room):
        room.description += 'The ceiling is made of stone. '
