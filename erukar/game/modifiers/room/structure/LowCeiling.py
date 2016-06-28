from erukar.engine.model import Modifier
from erukar.engine.environment import Room
from erukar.game.modifiers.RoomModifier import RoomModifier

class LowCeiling(RoomModifier):
    Probability = 2
    def apply_to(self, room):
        room.description += 'The ceiling of the room is lower than normal. '
