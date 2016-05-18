from pynarpg.model.DirectionalCommand import DirectionalCommand
from pynarpg.environment.Door import Door
from pynarpg.environment.Room import Room

class Move(DirectionalCommand):
    move_through_wall = 'You attempt to pass through a wall with no luck'
    move_through_closed_door = 'You cannot move this way because a door prevents you from doing so'
    move_successful = 'You have successfully moved'

    def execute(self, payload):
        player = self.find_player()
        direction = self.determine_direction(payload.lower())
        in_direction = player.character.current_room.get_in_direction(direction)

        # No connections have been made in this direction
        if in_direction is None:
            return Move.move_through_wall

        # determine if the door prevents movement
        door = in_direction["door"]
        if door is not None and door.status is not Door.Open:
            return Move.move_through_closed_door

        # Move and autoinspect the room for the player
        player.character.current_room = in_direction['room']
        player.character.current_room.on_inspect(player)
        return Move.move_successful
