from erukar.engine.model import Modifier
from erukar.engine.environment import *
from erukar.game.modifiers.RoomDoorModifier import RoomDoorModifier
import random

class Archway(RoomDoorModifier):
    Probability = 100
    def __init__(self):
        self.description = "An archway to the {0} opens into another room."
        self.can_close = False
        self.start_state = Door.Open
