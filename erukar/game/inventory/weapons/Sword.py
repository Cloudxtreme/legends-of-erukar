from erukar.engine.inventory.Weapon import Weapon

class Sword(Weapon):
    Probability = 1
    BaseName = "Sword"

    def __init__(self):
        super().__init__(Sword.BaseName)
        self.damage = '1d6'
