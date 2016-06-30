from erukar.engine.model.RpgEntity import RpgEntity

class Item(RpgEntity):
    generic_description = 'This {0} is {2}, but otherwise has no real description whatsoever'

    def __init__(self, item_type='Item', name="Item"):
        self.item_type = item_type
        self.name = name
        self.price = 0
        self.rarity = 'Generic'
        self.suffix = ''
        self.description = Item.generic_description

    def describe(self):
        return '{0} {1} {2}'.format(self.rarity, self.name, self.suffix).strip()

    def matches(self, other):
        return other.lower() in self.get_name().lower() \
            or other.lower() in self.item_type.lower()

    def on_inspect(self, sender):
        return self.description.format(*(self.name, self.suffix, self.rarity))

    def get_name(self):
        return self.name
