from erukar.engine.model import Modifier
from erukar.engine.environment import *
from erukar.game.modifiers.RoomModifier import RoomModifier
from erukar.engine.environment.Door import Door
import random

class RoomDoorModifier(RoomModifier):
    def __init__(self):
        self.description = "A door to the {0} opens into another room."
        self.can_close = False
        self.start_state = Door.Open

    def apply_to(self, room):
        rooms = [r for r in room.connections if room.connections[r]['room'] is not None and room.connections[r]['door'] is None]
        if len(rooms) == 0: return

        direction = random.choice(rooms)
        thisdoor = Door(self.description)
        thisdoor.status = self.start_state
        thisdoor.can_close = self.can_close
        room.add_door(direction, thisdoor)
