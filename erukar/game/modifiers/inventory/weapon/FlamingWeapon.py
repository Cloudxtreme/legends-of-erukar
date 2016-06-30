from erukar.game.modifiers.WeaponMod import WeaponMod
from erukar.engine.inventory import Weapon

class FlamingWeapon(WeaponMod):
    Probability = 5
    def apply_to(self, weapon):
        weapon.name += " of the Flames"
