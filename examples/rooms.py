from erukar import *
from examples.helpers.ExampleRunner import ExampleRunner

print('Room Generation Example: Basically just a randomly generated hallway right now')

runner = ExampleRunner()
d = DungeonGenerator()

dungeon = d.generate()
runner.set_room(dungeon.rooms[0])
runner.start()
