from erukar.engine.model import Modifier
from erukar.engine.environment import Room
from erukar.game.modifiers.RoomModifier import RoomModifier

class BrightLight(RoomModifier):
    Probability = 1
    def apply_to(self, room):
        room.description += 'The light in this room is incredibly bright. '
