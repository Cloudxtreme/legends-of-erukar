from pynarpg.model.RpgEntity import RpgEntity

class Item(RpgEntity):
    generic_description = 'This {0} is {2}, but otherwise has no real description whatsoever'

    def __init__(self, item_type='Item'):
        self.item_type = item_type
        self.price = 0
        self.rarity = 'Generic'
        self.suffix = ''
        self.description = Item.generic_description

    def describe(self):
        return '{0} {1} {2}'.format(self.rarity, self.item_type, self.suffix).strip()

    def matches(self, other):
        return self.get_name().lower() in other.lower()

    def on_inspect(self, sender):
        return self.description.format(*(self.item_type, self.suffix, self.rarity))

    def get_name(self):
        return self.item_type
