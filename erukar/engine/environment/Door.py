from erukar.engine.model.RpgEntity import RpgEntity

class Door(RpgEntity):
    Closed = 0
    Open = 1
    Locked = 2

    def __init__(self):
        self.status = Door.Closed

    def on_inspect(self, direction):
        return "This is a door to the {0}".format(direction)
