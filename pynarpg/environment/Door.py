from pynarpg.model.EnvironmentPiece import EnvironmentPiece
from pynarpg.model.Interactible import Interactible

class Door(EnvironmentPiece, Interactible):
    Closed = 0
    Open = 1
    Locked = 2

    def __init__(self):
        self.status = Door.Closed

    def on_inspect(self, *_):
        return "This is a door"

    def on_open(self, *_):
        '''Used when the system receives an 'Open' command'''
        if self.status is Door.Open:
            return 'Door is already open'

        if self.status is Door.Locked:
            return 'Door cannot be opened because it is locked'

        self.status = Door.Open
        return 'Door opened'
