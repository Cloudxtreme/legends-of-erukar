from pynarpg.model.RpgEntity import RpgEntity
from pynarpg.model.EntityLocation import EntityLocation

class Containable(RpgEntity):
    def __init__(self):
        self.contents = []
        self.description = ""

    def add(self, item, adjective, preposition, plural=False):
        self.contents.append(EntityLocation(item, adjective, preposition, plural))

    def describe(self):
        return ' '.join([self.description] + [c.describe() for c in self.contents if c.describe() is not None])

    def remove(self, entity):
        target = next((x for x in self.contents if x is entity or (hasattr(x, 'entity') and x.entity is entity)), None)
        self.contents.remove(entity)
