class DataAccess:
    def __init__(self):
        self.players = []

    def find_player(self, uid):
        return next((p for p in self.players if p.uid == uid), None)
