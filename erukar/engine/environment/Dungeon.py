from erukar.engine.model.RpgEntity import RpgEntity

class Dungeon(RpgEntity):
    minimum_rooms = 3

    def __init__(self):
        self.dungeon_map = {}
        self.rooms = []
