from erukar.engine.model import Modifier
from erukar.engine.environment import Room
from erukar.game.modifiers.RoomModifier import RoomModifier

class StoneWalls(RoomModifier):
    def apply_to(self, room):
        room.description += ' The walls are made of stone.'
