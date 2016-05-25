from pynarpg.engine.commands.Inspect import Inspect
from pynarpg.engine.commands.DirectionalCommand import DirectionalCommand
from pynarpg.engine.environment.Door import Door
from pynarpg.engine.environment.Room import Room

class Move(DirectionalCommand):
    move_through_wall = 'You attempt to pass through a wall with no luck'
    move_through_closed_door = 'You cannot move this way because a door prevents you from doing so'
    move_successful = 'You have successfully moved {0}.\n\n{1}'

    def execute(self, payload):
        player = self.find_player()
        direction = self.determine_direction(payload.lower())
        if direction is None: return ''
        in_direction = player.character.current_room.get_in_direction(direction)

        # No connections have been made in this direction
        if in_direction is None:
            return Move.move_through_wall

        # determine if the door prevents movement
        door = in_direction['door']
        if door is not None and door.status is not Door.Open:
            return Move.move_through_closed_door

        # Move and autoinspect the room for the player
        return self.change_room(player, in_direction['room'], direction)

    def change_room(self, player, new_room, direction):
        '''Used to transfer the character from one room to the next'''
        character = player.character
        if character in character.current_room.contents:
            character.current_room.contents.remove(character)
        new_room.contents.append(character)
        character.current_room = new_room

        i = Inspect()
        i.data = self.data
        i.sender_uid = self.sender_uid
        inspection_result = i.execute('')

        return Move.move_successful.format(direction.name, inspection_result)
