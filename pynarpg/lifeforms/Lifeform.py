from pynarpg.model.RpgEntity import RpgEntity

class Lifeform(RpgEntity):
    base_armor_class = 10
    base_health = 4

    def __init__(self):
        self.attributes = {'str': -2, 'dex': -2, 'vit': -2}
        self.afflictions = []
        self.armor = None
        self.weapon = None
        self.level = 0
        self.health = 0
        self.current_room = None

    def define_stats(self, strength=-2, dexterity=-2, vitality=-2):
        self.attributes = { 'str': strength, 'dex': dexterity, 'vit': vitality }

    def define_level(self, level):
        self.level = level
        self.health = sum([Lifeform.base_health + self.attributes['vit']\
            for x in range(0, level)])

    def calculate_armor_class(self):
        if self.armor is not None:
            return self.armor.calculate_armor_class(self.attributes['dex'])
        return Lifeform.base_armor_class + self.attributes['dex']

    def skill_roll_string(self, skill_type):
        skill_value = self.attributes[skill_type]
        if(skill_value < 0):
            return '1d20{0}'.format(skill_value)
        return '1d20+{0}'.format(skill_value)

    def attack(self, target):
        '''Attack another lifeform'''
        # Send a message that the player cannot attack without a weapon
        if self.weapon is None: return

        attack_roll = self.roll(self.skill_roll_string('dex'))
        armor_class = target.calculate_armor_class()
        damage = self.weapon.roll()

        return [attack_roll, armor_class, damage]

    def take_damage(self, damage):
        if 'dying' in self.afflictions:
            self.kill()
        self.health = max(0, self.health - damage)
        if self.health == 0:
            self.afflictions.append('dying')

    def kill(self):
        self.afflictions = ['dead']
