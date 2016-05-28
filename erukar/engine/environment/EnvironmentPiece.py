from erukar.engine.model.RpgEntity import RpgEntity
import random

class EnvironmentPiece(RpgEntity):
    def __init__(self, aliases, inspect_results):
        super().__init__()
        self.aliases = aliases
        self.description = inspect_results

    def on_inspect(self, *_):
        return self.describe()

    def matches(self, query):
        return any([query in alias for alias in self.aliases])

    def describe(self):
        return self.description

    def get_name(self):
        return random.choice(self.aliases)
