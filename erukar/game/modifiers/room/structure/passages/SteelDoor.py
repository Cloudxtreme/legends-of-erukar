from erukar.game.modifiers.RoomDoorModifier import RoomDoorModifier
from erukar import Door

class SteelDoor(RoomDoorModifier):
    Probability = 1
    def __init__(self):
        self.description = "There is a steel door to the {0}."
        self.can_close = True
        self.start_state = Door.Closed
