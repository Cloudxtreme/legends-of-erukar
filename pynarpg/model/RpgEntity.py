import math, random, re

class RpgEntity:
    expression = '(\d+)d(\d+)([+-]\d+)?'

    def regex(self, to_evaluate):
        '''Regex on the damage string'''
        captured = re.search(RpgEntity.expression, to_evaluate)
        return [int(x) for x in captured.groups() if x is not None]

    def roll(self, to_evaluate):
        regex = self.regex(to_evaluate)
        num, die = regex[:2]
        modifier = 0
        if len(regex) == 3:
            modifier = regex[2]
        return sum([self.individual_roll(die) + modifier for x in range(0,num)])

    def individual_roll(self, die):
        '''Perform a single roll of a die'''
        return math.ceil(random.uniform(0, die))
