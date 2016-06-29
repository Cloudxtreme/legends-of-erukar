from erukar import *
from examples.helpers.ExampleRunner import ExampleRunner

print('Room Generation Example: Basically just a randomly generated hallway right now\n')

runner = ExampleRunner()
d = DungeonGenerator()
dungeon = d.generate()

# Now Decorate the dungeon
base_module = "erukar.game.modifiers.room.{0}"
sub_modules = [
    "materials.floors",
    "materials.walls",
    "materials.ceilings",
    "structure.ceilings",
    "contents.decorations",
    "contents.items",
    "structure.passages",
    "phenomena",
    "qualities.air",
    "qualities.lighting",
    "qualities.sounds"]

decorators = [RoomDecorator(base_module.format(sm)) for sm in sub_modules]

for room in dungeon.rooms:
    for decorator in decorators:
        decorator.apply_one_to(room)

runner.set_room(dungeon.rooms[0])
runner.start()
