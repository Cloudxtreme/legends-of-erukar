from pynarpg.model.DirectionalCommand import DirectionalCommand
from pynarpg.environment.Door import Door

class Close(DirectionalCommand):
    nesw_success = 'You have successfully closed the door'
    nesw_locked = 'You try to close the door, but it is locked'
    nesw_already_closed = 'The door is already closed'
    nesw_no_door = 'There is no door in this direction to close'
    nesw_wall = 'You cannot close a wall'
    not_found = 'There is nothing to close'

    # I'm not terribly happy with this, as it forces usage of only Doors.
    def execute(self, room, payload):
        player = self.find_player()
        direction = self.determine_direction(payload.lower())

        # If the payload was NESW, treat this as a door
        if direction is not None:
            return self.handle_doors(room, direction)

        # Otherwise we need to find in the room
        return self.handle_contents(room, player, payload)

    def handle_contents(self, room, player, item_name):
        '''Try to find the item in the room, then run on_close on it if so'''
        item = self.find_in_room(room, item_name)
        if item is not None:
            # We found it, so run on_close on it
            return item.on_close(player)

        # Send a failure message
        return Close.not_found

    def handle_doors(self, room, direction):
        '''
        Treat this command as an close doors command, since the user typed in
        a direction
        '''
        in_direction = room.get_in_direction(direction)

        # No connections have been made in this direction
        if in_direction is None:
            return Close.nesw_wall

        # determine if the door prevents movement
        door = in_direction["door"]
        if door is None:
            # There is no door to close
            return Close.nesw_no_door

        # Door is locked
        if door.status is Door.Locked:
            return Close.nesw_locked

        # Door is already close
        if door.status is Door.Closed:
            return Close.nesw_already_closed

        # Actually close the door
        door.status = Door.Closed
        return Close.nesw_success
