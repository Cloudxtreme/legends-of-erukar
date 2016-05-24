from pynarpg.model.DirectionalCommand import DirectionalCommand
from pynarpg.model.Containable import Containable
from pynarpg.model.EntityLocation import EntityLocation

class Inspect(DirectionalCommand):
    not_found = "Nothing matching '{0}' was found in this room."
    def __init__(self):
        super().__init__()

    def execute(self, payload):
        player = self.find_player()
        room = player.character.current_room
        self.index(room, player)
        direction = self.determine_direction(payload.lower())

        if direction is None:
            if payload in ['','room']: return room.describe()
            item = self.find_in_room(room, payload)
            if item is None:
                return Inspect.not_found.format(payload)
            return self.inspect_item(item, player)

        return room.nesw_descriptions[direction]

    def inspect_item(self, item, player):
        if type(item) is EntityLocation:
            item = item.entity
        self.index(item, player)
        return item.on_inspect(player)

    def index(self, container, player):
        if issubclass(type(container), Containable):
            for i in container.contents:
                player.index_item(i, container)
