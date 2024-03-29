from erukar.engine.commands.Inspect import Inspect
from erukar.engine.commands.DirectionalCommand import DirectionalCommand
from erukar.engine.environment import *

class Move(DirectionalCommand):
    move_through_wall = 'You attempt to pass through a wall with no luck'
    move_through_closed_door = 'You cannot move this way because a door prevents you from doing so'
    move_successful = 'You have successfully moved {0}.\n\n{1}'

    def execute(self, payload):
        player = self.find_player()
        direction = self.determine_direction(payload.lower())
        if direction is None: return ''
        in_direction = player.character.current_room.get_in_direction(direction)

        # determine if the door prevents movement
        door = in_direction.door
        if door is not None:
            if type(door) is Door and door.status is not Door.Open:
                return Move.move_through_closed_door
            if type(door) is Surface:
                return Move.move_through_wall

        # Move and autoinspect the room for the player
        if in_direction.room is None:
            return Move.move_through_wall
        return self.change_room(player, in_direction.room, direction)

    def change_room(self, player, new_room, direction):
        '''Used to transfer the character from one room to the next'''
        player.move_to_room(new_room)

        i = Inspect()
        i.data = self.data
        i.sender_uid = self.sender_uid
        inspection_result = i.execute('')

        return Move.move_successful.format(direction.name, inspection_result)
