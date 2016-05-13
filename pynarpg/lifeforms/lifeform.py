from pynarpg.model.RpgEntity import RpgEntity

class Lifeform(RpgEntity):
    def __init__(self):
        self.attributes = {}
        self.armor = None
        self.weapon = None
        self.level = 0
        self.health = 0

    def define_stats(self, strength=-2, dexterity=-2, vitality=-2):
        self.attributes = { 'str': strength, 'dex': dexterity, 'vit': vitality }

    def define_level(self, level):
        self.level = level
        self.health = sum([4+self.attributes['vit'] for x in range(0, level)])

    def calculate_armor_class(self):
        if self.armor is not None:
            return self.armor.calculate_armor_class()
        return 8 + self.attributes['dex']

    def attack(self, target):
        '''Attack another lifeform'''
        # Send a message that the player cannot attack without a weapon
        if self.weapon is None: return

        self.weapon.roll()
