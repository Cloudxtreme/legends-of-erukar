from erukar.engine.model import Modifier
from erukar.engine.environment import Room
from erukar.game.modifiers.RoomModifier import RoomModifier

class WoodFloor(RoomModifier):
    Probability = 3
    
    def apply_to(self, room):
        room.description += 'The floor is made of some sort of ambiguous wood. '
