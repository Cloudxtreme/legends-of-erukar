from pynarpg.model.RpgEntity import RpgEntity

class Inventory(RpgEntity):
    def __init__(self):
        self.price = 0
        self.name = 'Generic Item'
