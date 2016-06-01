from erukar import *
from examples.helpers.ExampleRunner import ExampleRunner

print('Room Generation Example: Basically just a randomly generated hallway right now')

runner = ExampleRunner()
d = DungeonGenerator()

rooms = d.generate()
runner.set_room(rooms[0])
runner.start()
