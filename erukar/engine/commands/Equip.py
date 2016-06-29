from erukar.engine.model.Command import Command
from erukar.engine.inventory.Armor import Armor
from erukar.engine.inventory.Weapon import Weapon
import re

class Equip(Command):
    not_found = "Unable to find '{0}' in inventory"
    equipped_weapon = "'{0}' equipped as weapon successfully"
    equipped_armor = "'{0}' equipped as armor successfully"
    cannot_equip = "'{0}' was found but cannot be equipped"
    item_type_expression = "\.(\w+)'"

    def execute(self, item_name):
        player = self.find_player()
        if player is None: return

        # Get the item from our inventory if it exists
        item = self.find_in_inventory(player, item_name)
        if item is None:
            return Equip.not_found.format(item_name)

        # Check to see if the item's type exists as a field on the character
        item_type = item.item_type
        if hasattr(player.character, item_type):
            setattr(player.character, item_type, item)
            return getattr(Equip, 'equipped_{0}'.format(item_type)).format(item.describe())

        return Equip.cannot_equip.format(item.describe())

    def item_type(self, item):
        '''Get the lower case item type as a string'''
        captured = re.search(Equip.item_type_expression, str(type(item)))
        return captured.groups()[0].lower()
