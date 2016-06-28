from erukar.engine.model import Modifier
from erukar.engine.environment import *
from erukar.game.modifiers.RoomModifier import RoomModifier

class WaterDrops(RoomModifier):
    Probability = 1
    def apply_to(self, room):
        room.description += 'You hear droplets of water falling from somewhere in the room. '
        deco = Decoration(aliases=['water droplets', 'drops of water', 'droplets of water'], \
            inspect_results='The water appears to be dripping from somewhere above you. The source is otherwise undeterministic. ')
        room.add(article='a', item=deco, preposition='on the floor')
