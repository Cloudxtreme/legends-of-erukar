from pynarpg.model.Command import Command
from pynarpg.inventory.Armor import Armor
from pynarpg.inventory.Weapon import Weapon

class Equip(Command):
    not_found = "Unable to find '{0}' in inventory"
    equipped_weapon = "'{0}' equipped as weapon successfully"
    equipped_armor = "'{0}' equipped as armor successfully"
    cannot_equip = "'{0}' was found but cannot be equipped"

    def execute(self, room, item_name):
        player = self.find_player()
        if player is None: return

        item = self.find_in_inventory(player, item_name)
        if item is None:
            return Equip.not_found.format(item_name)

        if type(item) is Weapon:
            player.character.weapon = item
            return Equip.equipped_weapon.format(item.describe())

        if type(item) is Armor:
            player.character.armor = item
            return Equip.equipped_armor.format(item.describe())

        return Equip.cannot_equip.format(item.describe())
