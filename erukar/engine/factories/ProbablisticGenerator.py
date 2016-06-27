from erukar.engine.factories.FactoryBase import FactoryBase
from erukar.engine.environment import *
import numpy as np
import math, random

class ProbablisticGenerator(FactoryBase):
    def __init__(self):
        self.bins = []
        self.values = []

    def create_distribution(self, possibilities, weights):
        '''
        The possibilities and weights must be lists in the same order
        '''
        total_weight = sum(weights)
        self.bins = np.array([x/total_weight for x in np.add.accumulate(weights)])
        self.values = np.array(possibilities)

    def create_one(self):
        return self.values[np.digitize(random.uniform(0, 1), self.bins)]
