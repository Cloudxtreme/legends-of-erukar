from pynarpg.model.Command import Command

class Take(Command):
    def execute(self, room, item_name):
        player = self.find_player()
        item = self.find_in_room(room, item_name)
        if item is not None and player is not None:
            player.character.inventory.append(item)
            room.contents.remove(item)

    def find_in_room(self, room, item_name):
        results = [p for p in room.contents if p.matches(item_name)]
        if len(results) > 0:
            return results[0]
