from erukar.engine.model import Modifier
from erukar.engine.environment import Room

class RoomModifier(Modifier):
    def __init__(self):
        super().__init__()
        self.permission_type = Modifier.ALL_PERMITTED
        self.permitted_entities.append(Room)

    def apply_to(self, room):
        room.description += ' The air is dusty.'
