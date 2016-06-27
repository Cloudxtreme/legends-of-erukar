from erukar.engine import ProbablisticGenerator
from erukar.game.modifiers.room import *

class RoomDecorator(ProbablisticGenerator):
    possibilities = [
        (2, Dusty),
        (2, Small),
        (1, StillAir),
        (1, WaterDrops),
        (2, StoneWalls),
        (2, WoodFloor)]

    def __init__(self):
        super().__init__()
        weights, values = zip(*RoomDecorator.possibilities)
        self.create_distribution(values, weights)
