from erukar.engine.model import Modifier
from erukar.engine.environment import Room
from erukar.game.modifiers.RoomModifier import RoomModifier

class NoLight(RoomModifier):
    Probability = 1
    def apply_to(self, room):
        room.description += 'There is absolutely no light in this room. '
