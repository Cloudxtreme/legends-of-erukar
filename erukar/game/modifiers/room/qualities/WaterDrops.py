from erukar.engine.model import Modifier
from erukar.engine.environment import Room
from erukar.game.modifiers.RoomModifier import RoomModifier

class WaterDrops(RoomModifier):
    def apply_to(self, room):
        room.description += 'Droplets of water fall from a crack in the ceiling. '
