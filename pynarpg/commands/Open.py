from pynarpg.model.DirectionalCommand import DirectionalCommand
from pynarpg.environment.Door import Door

class Open(DirectionalCommand):
    nesw_success = 'You have successfully opened the door'
    nesw_locked = 'You try to open the door, but it is locked'
    nesw_already_open = 'The door is already open'
    nesw_no_door = 'There is no door in this direction to open'
    nesw_wall = 'You cannot open a wall'
    not_found = 'There is nothing to open'

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
        # Try to find the item in the room
        item = self.find_in_room(room, item_name)
        if item is not None:
            # We found it, so run on_open on it
            return item.on_open(player)

        # Send a failure message
        return Open.not_found

    def handle_doors(self, room, direction):
        '''
        Treat this command as an open doors command, since the user typed in
        a direction
        '''
        in_direction = room.get_in_direction(direction)

        # No connections have been made in this direction
        if in_direction is None:
            return Open.nesw_wall

        # determine if the door prevents movement
        door = in_direction["door"]
        if door is None:
            # There is no door to open
            return Open.nesw_no_door

        # Door is locked
        if door.status is Door.Locked:
            return Open.nesw_locked

        # Door is already open
        if door.status is Door.Open:
            return Open.nesw_already_open

        # Actually open the door
        door.status = Door.Open
        return Open.nesw_success
