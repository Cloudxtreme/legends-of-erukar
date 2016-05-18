from pynarpg.model.RpgEntity import RpgEntity

class Item(RpgEntity):
    def __init__(self, item_type='Item'):
        self.item_type = item_type
        self.price = 0
        self.rarity = 'Generic'
        self.suffix = ''

    def describe(self):
        return '{0} {1} {2}'.format(self.rarity, self.item_type, self.suffix).strip()

    def matches(self, other):
        return self.item_type.lower() in other.lower()
