class DataAccess:
    def __init__(self):
        self.players = []

    def find_player(self, uid):
        results = [p for p in self.players if p.uid == uid]
        if len(results) > 0:
            return results[0]
