from erukar.game.modifiers.RoomModifier import RoomModifier
from erukar.engine.environment.Surface import Surface

class MarbleFloor(RoomModifier):
    Probability = 1

    def apply_to(self, room):
        room.floor = Surface('The floor is made of a dense marble which seems to be polished.')
