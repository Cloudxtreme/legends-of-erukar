from pynarpg.model.Command import Command

class Take(Command):
    failure = "No item '{0}' was found"
    success = "Successfully took {0}"

    def execute(self, room, item_name):
        player = self.find_player()
        if player is None: return

        # Try to find the item in the room
        item = self.find_in_room(room, item_name)
        if item is not None:
            # We found it, so give it to the player and return a success msg
            player.character.inventory.append(item)
            room.contents.remove(item)
            return Take.success.format(item.describe())

        # Send a failure message
        return Take.failure.format(item_name)
