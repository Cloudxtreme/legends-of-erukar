from erukar import *
from examples.helpers.ExampleRunner import ExampleRunner

print('Room Generation Example: Basically just a randomly generated hallway right now\n')

runner = ExampleRunner()
d = DungeonGenerator()
dungeon = d.generate()

# Now Decorate the dungeon
materials = RoomDecorator('erukar.game.modifiers.room.materials')
qualities = RoomDecorator('erukar.game.modifiers.room.qualities')
for room in dungeon.rooms:
    materials.create_one().apply_to(room)
    qualities.create_one().apply_to(room)

runner.set_room(dungeon.rooms[0])
runner.start()
