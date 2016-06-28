from erukar.engine.model import Modifier
from erukar.engine.environment import Room
from erukar.game.modifiers.RoomModifier import RoomModifier

class DirtFloor(RoomModifier):
    Probability = 2

    def apply_to(self, room):
        room.description += 'The flooring of this room is packed dirt. '
