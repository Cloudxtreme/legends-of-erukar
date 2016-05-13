from pynarpg.inventory.inventory import Inventory
import math, random, re

class Weapon(Inventory):
    def __init__(self):
        self.damage = '1d6'
        self.damage_modifier = 'str'
        self.expression = '(\d+)d(\d+)([+-]\d+)?' # Make constant

    def regex(self):
        '''Regex on the damage string'''
        captured = re.search(self.expression, self.damage)
        return [int(x) for x in captured.groups() if x is not None]

    def roll(self):
        regex = self.regex()
        num, die = regex[:2]
        if len(regex) == 3:
            modifier = regex[3]
        return sum([self.individual_roll(die) + modifier for x in range(0,num)])

    def individual_roll(self, die):
        '''Perform a single roll of a die'''
        return math.ceil(random.uniform(0, die))
