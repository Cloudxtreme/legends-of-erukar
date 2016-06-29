from erukar.engine.model import Modifier
from erukar.engine.environment import Room
from erukar.game.modifiers.RoomModifier import RoomModifier

class HighCeiling(RoomModifier):
    Probability = 2
    def apply_to(self, room):
        room.ceiling.description += 'The ceiling of the room is higher than normal. '
