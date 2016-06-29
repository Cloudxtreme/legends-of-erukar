from erukar.engine.commands.DirectionalCommand import DirectionalCommand
from erukar.engine.model.Containable import Containable

class Inspect(DirectionalCommand):
    not_found = "Nothing matching '{0}' was found in this room."
    abyss = "There is nothing to your {0} except the abyss... plain and nothingness forever."
    def __init__(self):
        super().__init__()

    def execute(self, payload):
        player = self.find_player()
        room = player.character.current_room
        self.index(room, player)
        direction = self.determine_direction(payload.lower())

        if direction is None:
            return self.inspect_in_room(player, room, payload)

        result = room.describe_in_direction(direction, inspect_walls=True)
        if result is not None:
            return result

        return Inspect.abyss.format(direction.name)

    def inspect_in_room(self, player, room, payload):
        '''Used if the player didn't specify a direction'''
        if payload in ['','room']:
            return room.describe()

        if payload in 'flooring':
            return room.floor.on_inspect()

        if payload in 'ceiling':
            return room.ceiling.on_inspect()

        item = self.find_in_room(room, payload)
        if item is not None:
            return self.inspect_item(item, player)

        return Inspect.not_found.format(payload)

    def inspect_item(self, item, player):
        '''Inspect an item and index it if it's a container'''
        self.index(item, player)
        return item.on_inspect(player)

    def index(self, container, player):
        '''Indexes all items in a container for the PlayerNode's indexer'''
        if issubclass(type(container), Containable):
            for i in container.contents:
                player.index_item(i, container)
