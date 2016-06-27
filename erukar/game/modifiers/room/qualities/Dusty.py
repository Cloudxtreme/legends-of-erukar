from erukar.engine.model import Modifier
from erukar.engine.environment import Room
from erukar.game.modifiers.RoomModifier import RoomModifier

class Dusty(RoomModifier):
    def apply_to(self, room):
        room.description += ' The air is dusty.'
