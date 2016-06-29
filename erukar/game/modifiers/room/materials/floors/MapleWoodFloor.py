from erukar.game.modifiers.RoomModifier import RoomModifier
from erukar.engine.environment.Surface import Surface

class MapleWoodFloor(RoomModifier):
    Probability = 2

    def apply_to(self, room):
        room.floor = Surface('The floor is made of maple hardwood.')
