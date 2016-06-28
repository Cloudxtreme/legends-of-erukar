from erukar.engine.model.Containable import Containable

class Container(Containable):
    def __init__(self, aliases, broad_results, inspect_results):
        super().__init__(aliases, broad_results, inspect_results)
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
