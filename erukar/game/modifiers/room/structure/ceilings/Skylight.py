from erukar.engine.model import Modifier
from erukar.engine.environment import Room
from erukar.game.modifiers.RoomModifier import RoomModifier

class Skylight(RoomModifier):
    Probability = 0.2
    def apply_to(self, room):
        room.description += 'The ceiling of this room opens up to the outside, but it is too far for you to climb out safely. '
