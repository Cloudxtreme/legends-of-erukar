from erukar.game.modifiers.RoomModifier import RoomModifier
from erukar.game.decorators.RoomDecorator import RoomDecorator
from erukar.engine.environment import *

class Weapon(RoomModifier):
    Probability = 10

    def apply_to(self, room):
        randomizer = RoomDecorator('erukar.game.inventory.weapons')
        room.add(randomizer.create_one())
