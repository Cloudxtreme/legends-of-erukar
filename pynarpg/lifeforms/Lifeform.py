from pynarpg.model.RpgEntity import RpgEntity

class Lifeform(RpgEntity):
    attribute_types = ["strength", "dexterity", "vitality"]
    attribute_value_default = -2
    attack_damage_attribute = "strength"
    attack_roll_attribute = "dexterity"
    armor_attribute = "dexterity"
    health_attribute = "vitality"
    equipment_types = ["armor", "weapon"]
    base_armor_class = 10
    base_health = 4

    def __init__(self, name=""):
        for att in Lifeform.attribute_types:
            setattr(self, att, Lifeform.attribute_value_default)
        self.level, self.health = [0, 0]
        self.armor, self.weapon, self.current_room = [None, None, None]
        self.name = name
        self.afflictions = []
        self.contents_map = {}

    def define_stats(self, stats):
        '''Takes a dictionary to define stats.'''
        for stat in [stat for stat in stats if hasattr(self, stat)]:
            setattr(self, stat, stats[stat])

    def define_level(self, level):
        '''Set this lifeform's level and defined the health appropriately'''
        self.level = level
        self.health = sum([Lifeform.base_health + self.get(Lifeform.health_attribute) for x in range(0, level)])

    def calculate_armor_class(self):
        if 'dying' in self.afflictions:
            return Lifeform.base_armor_class

        ac_mod = self.get(Lifeform.armor_attribute)
        if self.armor is not None:
            return self.armor.calculate_armor_class(ac_mod)
        return Lifeform.base_armor_class + ac_mod

    def skill_roll_string(self, skill_type):
        skill_value = self.get(skill_type)
        if(skill_value < 0):
            return '1d20{0}'.format(skill_value)
        return '1d20+{0}'.format(skill_value)

    def get(self, attribute):
        '''Alias for getattr(self, ____)'''
        return getattr(self, attribute)

    def matches(self, payload):
        return payload.lower() in self.name.lower()

    def get_name(self):
        return self.name

    def attack(self, target):
        '''Attack another lifeform'''
        # Send a message that the player cannot attack without a weapon
        armor_class = target.calculate_armor_class()
        if self.weapon is None: return [0, armor_class, 0]

        attack_roll = self.roll(self.skill_roll_string(Lifeform.attack_roll_attribute))
        damage = self.weapon.roll() + self.get(Lifeform.attack_damage_attribute)

        return [attack_roll, armor_class, damage]

    def take_damage(self, damage):
        if 'dying' in self.afflictions:
            self.kill()
            return

        self.health = max(0, self.health - damage)
        if self.health == 0:
            self.afflictions.append('dying')

    def kill(self):
        self.afflictions = ['dead']
