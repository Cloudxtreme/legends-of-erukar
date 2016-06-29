from erukar.game.modifiers.RoomModifier import RoomModifier
from erukar.engine.environment.Surface import Surface

class TiledFloor(RoomModifier):
    Probability = 3

    def apply_to(self, room):
        room.floor = Surface('The floor is made of ceramic times arranged in a checker pattern.')
