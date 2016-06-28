from erukar.engine.model import Modifier
from erukar.engine.environment import *
from erukar.game.modifiers.RoomModifier import RoomModifier

class WaterDrops(RoomModifier):
    Probability = 1
    def apply_to(self, room):
        deco = Decoration(aliases=['water droplets', 'drops of water', 'droplets of water'], \
            broad_results = 'You hear droplets of water falling from somewhere in the room',
            inspect_results='The water appears to be dripping from somewhere above you. The source is otherwise undeterministic. ')
        room.add(deco)
