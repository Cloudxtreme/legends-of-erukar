from pynarpg.lifeforms.Lifeform import Lifeform

class Player(Lifeform):
    def __init__(self):
        super().__init__()
        self.uid = '' # Player UID
        self.credits = 0
