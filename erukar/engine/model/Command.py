class Command:
    def __init__(self):
        self.sender_uid = ''
        self.data = None

    def execute(self, room, contents):
        '''Run this Command'''
        player = self.find_player()

    def find_player(self):
        '''Attempt to find a player in the data access component'''
        return self.data.find_player(self.sender_uid)

    def find_in_room(self, container, item_name):
        '''Attempt to find an item in a room's contents'''
        player = self.find_player()
        #directions = [container.connections[x]['door'] \
        #    for x in container.connections if container.connections[x] is not None]
        contents = set(container.contents + player.reverse_index(container))
        return next((p for p in contents if p.matches(item_name)), None)

    def find_in_inventory(self, player, item_name):
        '''Attempt to find an item in a player's inventory'''
        return next((p for p in player.character.inventory if p.matches(item_name)), None)
