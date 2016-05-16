import math, random, re

class RpgEntity:
    nDxy_expression = '(\d+)d(\d+)([+-]\d+)?'

    def regex(self, to_evaluate):
        '''Regex on the damage string'''
        captured = re.search(RpgEntity.nDxy_expression, to_evaluate)
        return [int(x) for x in captured.groups() if x is not None]

    def roll(self, to_evaluate):
        '''Roll on a string such as '1d20' or '6d6+6' '''
        regex = self.regex(to_evaluate)
        num, die, mod = [regex[i] if i < len(regex) else 0 for i in range(0,3)]
        return sum([self.individual_roll(die) + mod for x in range(0,num)])

    def individual_roll(self, die):
        '''Perform a single roll of a die (uniform distribution)'''
        return math.ceil(random.uniform(0, die))
