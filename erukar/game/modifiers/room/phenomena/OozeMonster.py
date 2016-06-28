from erukar.engine.model import Modifier
from erukar.engine.environment import Room
from erukar.engine.lifeforms import Lifeform
from erukar.game.modifiers.RoomModifier import RoomModifier

class OozeMonster(RoomModifier):
    Probability = 1
    def apply_to(self, room):
        l = Lifeform('Gray Ooze')
        l.define_level(1)
        room.add(article='a', item=l, preposition='on the floor')
        l.link_to_room(room)
