from erukar.engine.factories.FactoryBase import FactoryBase
from erukar.engine.environment import *
from erukar.engine.model import Direction
import numpy as np
import math, random

class DungeonGenerator(FactoryBase):
    minimum_rooms = 3

    def generate(self):
        num_rooms = math.floor(np.random.gamma(7.5, 1.0)) + DungeonGenerator.minimum_rooms
        return self.create_rooms(num_rooms)

    def create_rooms(self, num_rooms):
        rooms = [Room() for x in range(num_rooms)]

        # Make connections
        for origin, dest in zip(rooms, rooms[1:]):
            self.connect_randomly(origin, dest)

        # Add descriptions
        for r,i in zip(rooms, range(len(rooms))):
            r.description = 'This is the {0}th room'.format(i)

        # Fill in the abyss with walls (ugly, need to optimize)
        for room in rooms:
            for direction in self.possible_directions(room):
                room.connections[direction] = { 'door': Wall() }

        return rooms

    def connect_randomly(self, origin, destination):
        directions = self.possible_directions(destination)
        if not any(directions): return

        connect_dir = random.choice(directions)
        origin.coestablish_connection(connect_dir, destination)

    def possible_directions(self, room):
        return [d for d in room.connections if room.connections[d] is None]
