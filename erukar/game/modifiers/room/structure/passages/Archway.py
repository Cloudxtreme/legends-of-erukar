from erukar.engine.model import Modifier
from erukar.engine.environment import *
from erukar.game.modifiers.RoomModifier import RoomModifier
import random

class Archway(RoomModifier):
    Probability = 100
    def apply_to(self, room):
        rooms = [r for r in room.connections if room.connections[r]['room'] is not None]
        if len(rooms) == 0: return

        direction = random.choice(rooms)
        archway = Door("An archway to the {0} opens into another room.")
        archway.status = Door.Open
        archway.can_close = False
        room.connections[direction]['door'] = archway
