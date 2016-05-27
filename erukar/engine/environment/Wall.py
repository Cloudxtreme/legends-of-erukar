from erukar.engine.model.RpgEntity import RpgEntity

class Wall(RpgEntity):
    def on_inspect(self, direction):
        return "There is a wall to the {0}.".format(direction)
