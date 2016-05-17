from pynarpg.model.Command import Command
from pynarpg.inventory.Armor import Armor
from pynarpg.inventory.Weapon import Weapon

class Unequip(Command):
    def execute(self, room, item_name):
        player = self.find_player()
        if player is None: return

        if player.character.weapon is not None and player.character.weapon.matches(item_name):
            player.character.weapon = None
            return "Weapon has been unequipped"

        if player.character.armor is not None and player.character.armor.matches(item_name):
            player.character.armor = None
            return "Armor has been unequipped"

        return "No equipped item '{0}' was found".format(item_name)
