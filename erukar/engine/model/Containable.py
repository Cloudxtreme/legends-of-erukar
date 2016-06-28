from erukar.engine.model.RpgEntity import RpgEntity
from erukar.engine.model.EnvironmentPiece import EnvironmentPiece

class Containable(EnvironmentPiece):
    def __init__(self, aliases, broad_results, inspect_results):
        super().__init__(aliases, broad_results, inspect_results)
        self.contents = []
        self.description = ""

    def add(self, item):
        self.contents.append(item)

    def describe(self):
        return ' '.join([super().describe()] + [c.describe() for c in self.contents if c.describe() is not None])

    def remove(self, entity):
        target = next((x for x in self.contents if x == entity), None)
        self.contents.remove(target)
