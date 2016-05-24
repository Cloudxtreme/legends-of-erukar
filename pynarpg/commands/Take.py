from pynarpg.model.Command import Command
from pynarpg.inventory.Item import Item
from pynarpg.model.EntityLocation import EntityLocation

class Take(Command):
    failure = "No item '{0}' was found"
    cannot_take = "'{0}' cannot be taken."
    success = "Successfully took {0}"

    def execute(self, item_name):
        player = self.find_player()
        room = player.character.current_room
        if player is None: return

        # Try to find the item in the room
        item = self.find_in_room(room, item_name)
        if item is not None:
            return self.move_to_inventory(item, player, room)

        # Send a failure message
        return Take.failure.format(item_name)

    def move_to_inventory(self, item, player, room):
        if type(item) is EntityLocation:
            item = item.entity

        if not issubclass(type(item), Item):
            return Take.cannot_take.format(item.describe()).capitalize()

        # We found it, so give it to the player and return a success msg
        player.character.inventory.append(item)
        container = player.index(item)
        player.remove_index(item)
        if len(container) > 0:
            container[-1].remove(item)
        return Take.success.format(item.describe())
