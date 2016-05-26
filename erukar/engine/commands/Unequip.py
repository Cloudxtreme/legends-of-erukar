from erukar.engine.lifeforms.Lifeform import Lifeform
from erukar.engine.model.Command import Command
from erukar.engine.inventory.Armor import Armor
from erukar.engine.inventory.Weapon import Weapon

class Unequip(Command):
    not_found = "No equipped item '{0}' was found"
    unequipped_armor = "Armor has been unequipped"
    unequipped_weapon = "Weapon has been unequipped"

    def execute(self, item_name):
        player = self.find_player()
        if player is None: return

        # Try to unequip a specific type of equipment
        for equipment_type in Lifeform.equipment_types:
            result = self.unequip_type(player.character, equipment_type, item_name)
            if result is not None:
                return result

        # Nothing was found
        return Unequip.not_found.format(item_name)

    def unequip_type(self, character, equipment_type, item_name):
        '''Dynamic method to unequip a weapon or armor'''
        equipped = getattr(character, equipment_type)
        if equipped is None: return

        if equipped.matches(item_name):
            setattr(character, equipment_type, None)
            return getattr(Unequip, 'unequipped_{0}'.format(equipment_type))
