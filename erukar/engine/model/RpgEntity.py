from erukar.engine.model.Interactible import Interactible
import math, random, re

class RpgEntity(Interactible):
    nDxy_expression = '(\d+)d(\d+)([+-]\d+)?'
    base_armor_class = 10

    def regex(self, to_evaluate):
        '''Regex on the damage string'''
        captured = re.search(RpgEntity.nDxy_expression, to_evaluate)
        return [int(x) if x is not None else 0 for x in captured.groups()]

    def roll(self, to_evaluate):
        '''Roll on a string such as '1d20' or '6d6+6' '''
        num, die, mod = self.regex(to_evaluate)
        return sum([self.individual_roll(die) + mod for x in range(0,num)])

    def individual_roll(self, die):
        '''Perform a single roll of a die (uniform distribution)'''
        return math.ceil(random.random()*die)

    def calculate_armor_class(self):
        return RpgEntity.base_armor_class
