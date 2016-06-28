from erukar.engine import ProbablisticGenerator
from erukar.game.modifiers.room import *
import sys, inspect

class RoomDecorator(ProbablisticGenerator):
    def __init__(self, module):
        super().__init__()

        decoration_module = sys.modules[module]
        poss = [x[1] for x in inspect.getmembers(decoration_module, inspect.isclass)]

        weights, values = zip(*[(p.Probability, p) for p in poss])
        self.create_distribution(values, weights)
