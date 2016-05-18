from pynarpg.model.EnvironmentPiece import EnvironmentPiece
from pynarpg.model.Interactible import Interactible

class Door(EnvironmentPiece, Interactible):
    Closed = 0
    Open = 1
    Locked = 2

    def __init__(self):
        self.status = Door.Closed

    def on_inspect(self, *_):
        return "There is a door"
