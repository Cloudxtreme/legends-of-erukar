from erukar.engine.model import Modifier
from erukar.engine.environment import Room
from erukar.game.modifiers.RoomModifier import RoomModifier

class MapleWoodFloor(RoomModifier):
    Probability = 2

    def apply_to(self, room):
        room.description += 'The floor is made of maple hardwood. '
