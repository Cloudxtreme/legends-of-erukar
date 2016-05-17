from pynarpg.model.Command import Command
from pynarpg.inventory.Armor import Armor
from pynarpg.inventory.Weapon import Weapon

class Unequip(Command):
    not_found = "No equipped item '{0}' was found"
    unequipped_armor = "Armor has been unequipped"
    unequipped_weapon = "Weapon has been unequipped"

    def execute(self, room, item_name):
        player = self.find_player()
        if player is None: return

        if player.character.weapon is not None and player.character.weapon.matches(item_name):
            player.character.weapon = None
            return Unequip.unequipped_weapon

        if player.character.armor is not None and player.character.armor.matches(item_name):
            player.character.armor = None
            return Unequip.unequipped_armor

        return Unequip.not_found.format(item_name)
