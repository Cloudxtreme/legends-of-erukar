from erukar.game.modifiers.RoomDoorModifier import RoomDoorModifier
from erukar import Door

class Archway(RoomDoorModifier):
    Probability = 1
    def __init__(self):
        self.description = "An archway to the {0} opens into another room."
        self.can_close = False
        self.start_state = Door.Open
