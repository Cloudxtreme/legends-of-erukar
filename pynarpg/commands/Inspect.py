from pynarpg.model.DirectionalCommand import DirectionalCommand

class Inspect(DirectionalCommand):
    def __init__(self):
        super().__init__()

    def execute(self, payload):
        player = self.find_player()
        room = player.character.current_room
        direction = self.determine_direction(payload.lower())

        if direction is None:
            if payload is '': return room.describe()
            item = self.find_in_room(room, payload)
            if item is None:
                return room.describe()
            return item.on_inspect(player)

        return room.nesw_descriptions[direction]
