from erukar.game.modifiers.RoomModifier import RoomModifier
from erukar.game.decorators.RoomDecorator import RoomDecorator
from erukar.engine.environment import *

class Weapon(RoomModifier):
    Probability = 10

    def apply_to(self, room):
        randomizer = RoomDecorator('erukar.game.inventory.weapons')
        modifiers = RoomDecorator('erukar.game.modifiers.inventory.weapon')
        created_weapon = randomizer.create_one()
        modifiers.create_one().apply_to(created_weapon)
        room.add(created_weapon)
