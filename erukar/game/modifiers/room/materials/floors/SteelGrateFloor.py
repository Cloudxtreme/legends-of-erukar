from erukar.engine.model import Modifier
from erukar.engine.environment import Room
from erukar.game.modifiers.RoomModifier import RoomModifier

class SteelGrateFloor(RoomModifier):
    Probability = 0.1

    def apply_to(self, room):
        room.description += 'The floor of this room is comprised of a steel grate which seems to drop off into an abyss below you. '
