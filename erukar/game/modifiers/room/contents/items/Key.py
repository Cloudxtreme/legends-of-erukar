from erukar.game.modifiers.RoomModifier import RoomModifier
from erukar.engine.environment import *
import random

class Key(RoomModifier):
    Probability = 0
    materials = [
        'birch',
        'poplar'
        'maple',
        'ash',
        'mahogany',
        'walnut',
        'metallic']
    conditions = [
        "The table seems to have been made recently."]

    def __init__(self, material=None):
        if material is None:
            material = random.choice(Table.materials)
        self.material = material
        self.condition = random.choice(Table.conditions)

    def apply_to(self, room):
        location = random.choice(list(room.wall_directions()))
        deco = Decoration(aliases=['table', '{0} table'.format(self.material)], \
            broad_results = 'There is a {0} table to the {1} of the room'.format(self.material, location.name),
            inspect_results='This table is made of {0}. {1}'.format(self.material, self.condition))
        room.add(deco)
