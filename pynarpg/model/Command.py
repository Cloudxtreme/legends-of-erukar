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

    def find_in_room(self, room, item_name):
        '''Attempt to find an item in a room's contents'''
        results = [p for p in room.contents if p.matches(item_name)]
        if len(results) > 0:
            return results[0]

    def find_in_inventory(self, player, item_name):
        '''Attempt to find an item in a player's inventory'''
        results = [p for p in player.character.inventory if p.matches(item_name)]
        if len(results) > 0:
            return results[0]
