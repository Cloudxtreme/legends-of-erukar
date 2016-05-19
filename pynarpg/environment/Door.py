from pynarpg.model.EnvironmentPiece import EnvironmentPiece

class Door(EnvironmentPiece):
    Closed = 0
    Open = 1
    Locked = 2

    def __init__(self):
        self.status = Door.Closed

    def on_inspect(self, *_):
        return "There is a door"
