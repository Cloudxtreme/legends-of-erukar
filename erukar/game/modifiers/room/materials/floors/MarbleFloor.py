from erukar.engine.model import Modifier
from erukar.engine.environment import Room
from erukar.game.modifiers.RoomModifier import RoomModifier

class MarbleFloor(RoomModifier):
    Probability = 1

    def apply_to(self, room):
        room.description += 'The floor is made of a dense marble which seems to be polished. '
