from erukar.engine import ProbablisticGenerator
from erukar.game.modifiers.room import *

class RoomDecorator(ProbablisticGenerator):
    values = [
        Dusty,
        Small,
        StoneWalls,
        WoodFloor]

    weights = [
        1,
        1,
        1,
        2]

    def __init__(self):
        super().__init__()
        self.create_distribution(RoomDecorator.values, RoomDecorator.weights)
