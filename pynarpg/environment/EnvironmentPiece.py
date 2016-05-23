from pynarpg.model.RpgEntity import RpgEntity
import random

class EnvironmentPiece(RpgEntity):
    def __init__(self, aliases, description, results):
        super().__init__()
        self.aliases = aliases
        self.inspect_results = results
        self.description = description

    def on_inspect(self, *_):
        return self.inspect_results

    def matches(self, query):
        return any([query in alias for alias in self.aliases])

    def describe(self):
        return self.description

    def get_name(self):
        return random.choice(self.aliases)
