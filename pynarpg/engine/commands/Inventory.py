from pynarpg.engine.model.Command import Command
from pynarpg.engine.lifeforms.Lifeform import Lifeform

class Inventory(Command):
    header = 'INVENTORY\n----------\nWeapon:\t{1}\nArmor:\t{0}\n----------'
    item = "{0}.\t{1}"

    def execute(self, *_):
        char = self.find_player().character
        header = self.get_header(char)

        items = '\n'.join([Inventory.item.format(i, char.inventory[i].describe())\
            for i in range(0, len(char.inventory))])

        return header + '\n' + items

    def get_header(self, char):
        result = Inventory.header
        descriptions = (self.describe_attribute(char, item_type)\
            for item_type in Lifeform.equipment_types)
        return result.format(*descriptions)

    def describe_attribute(self, character, name):
        result = getattr(character, name)
        if result is not None:
            return result.describe()
