from erukar.game.modifiers.RoomModifier import RoomModifier
from erukar.engine.environment.Surface import Surface

class StoneCeilings(RoomModifier):
    Probability = 3

    def apply_to(self, room):
        room.ceiling = Surface('The ceiling is made of stone.')
