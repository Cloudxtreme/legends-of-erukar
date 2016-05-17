from pynarpg.model.Command import Command
from pynarpg.inventory.Armor import Armor
from pynarpg.inventory.Weapon import Weapon

class Equip(Command):
    def execute(self, room, item_name):
        player = self.find_player()
        if player is None: return

        item = self.find_in_inventory(player, item_name)
        if item is None:
            return "Unable to find '{0}' in inventory".format(item_name)

        if type(item) is Weapon:
            player.character.weapon = item
            return "'{0}' equipped as weapon successfully".format(item.describe())

        if type(item) is Armor:
            player.character.armor = item
            return "'{0}' equipped as armor successfully".format(item.describe())

        return "'{0}' was found but cannot be equipped".format(item.describe())
