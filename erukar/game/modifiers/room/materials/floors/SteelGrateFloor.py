from erukar.game.modifiers.RoomModifier import RoomModifier
from erukar.engine.environment.Surface import Surface

class SteelGrateFloor(RoomModifier):
    Probability = 0.1

    def apply_to(self, room):
        room.floor = Surface('The floor of this room is comprised of a steel grate which seems to drop off into an abyss below you.')
