from pynarpg.model.DirectionalCommand import DirectionalCommand

class Inspect(DirectionalCommand):
    def __init__(self):
        super().__init__()

    def execute(self, payload):
        player = self.find_player()
        room = player.character.current_room
        direction = self.determine_direction(payload.lower())

        if direction is None:
            return room.description

        return room.nesw_descriptions[direction]
