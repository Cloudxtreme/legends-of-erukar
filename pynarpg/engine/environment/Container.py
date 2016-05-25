from pynarpg.engine.model.Containable import Containable
from pynarpg.engine.environment.EnvironmentPiece import EnvironmentPiece

class Container(Containable, EnvironmentPiece):
    def __init__(self, aliases, description, results):
        Containable.__init__(self)
        self.aliases = aliases
        self.description = description
        self.results = results

    def on_open(self, sender):
        return "Opened a chest"

    def on_close(self, sender):
        return "Closed a chest"

    def describe(self):
        return EnvironmentPiece.describe(self)

    def on_inspect(self, *_):
        return Containable.describe(self)
