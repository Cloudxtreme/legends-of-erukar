from erukar.engine.model.Containable import Containable
from erukar.engine.environment.EnvironmentPiece import EnvironmentPiece

class Container(Containable, EnvironmentPiece):
    def __init__(self, aliases, inspect_results):
        Containable.__init__(self)
        self.aliases = aliases
        self.description = inspect_results

    def on_open(self, sender):
        return "Opened a chest"

    def on_close(self, sender):
        return "Closed a chest"

    def describe(self):
        return Containable.describe(self)

    def on_inspect(self, *_):
        return Containable.describe(self)
