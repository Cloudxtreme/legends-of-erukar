from erukar.engine.lifeforms.Lifeform import Lifeform

class Player(Lifeform):
    def __init__(self):
        super().__init__()
        self.uid = '' # Player UID
        self.inventory = []
        self.credits = 0
