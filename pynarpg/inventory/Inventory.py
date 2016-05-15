from pynarpg.model.RpgEntity import RpgEntity

class Inventory(RpgEntity):
    def __init__(self):
        self.item_type = 'Item'
        self.price = 0
        self.rarity = 'Generic'
        self.suffix = ''
