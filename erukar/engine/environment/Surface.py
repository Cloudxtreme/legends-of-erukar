from erukar.engine.model.RpgEntity import RpgEntity

class Surface(RpgEntity):
    def __init__(self, description="This is a wall."):
        self.description = description

    def on_inspect(self, *_):
        return self.description
