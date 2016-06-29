from erukar.engine.model import Modifier
from erukar.engine.environment import Room
from erukar.game.modifiers.RoomModifier import RoomModifier

class StoneWalls(RoomModifier):
    Probability = 3
    def apply_to(self, room):
        for wall in room.walls():
            wall.description = "This wall is made of stone"
