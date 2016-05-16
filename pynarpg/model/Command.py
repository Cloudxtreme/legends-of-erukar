class Command:
    def __init__(self):
        self.sender_uid = ''
        self.data = None

    def execute(self, room, contents):
        player = self.find_player()

    def find_player(self):
        return self.data.find_player(self.sender_uid)
