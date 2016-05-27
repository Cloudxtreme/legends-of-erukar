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
        '''Create X number of rooms'''
        rooms = [Room() for x in range(num_rooms)]
        self.connect_rooms(rooms)
        self.generate_descriptions(rooms)
        self.fill_walls(rooms)

        return rooms

    def connect_rooms(self, rooms):
        '''Connect a list of rooms to each other'''
        for origin, dest in zip(rooms, rooms[1:]):
            self.connect_randomly(origin, dest)

    def generate_descriptions(self, rooms):
        ''' Add descriptions '''
        for r,i in zip(rooms, range(len(rooms))):
            r.description = 'This is the {0}th room'.format(i)

    def fill_walls(self, rooms):
        '''Fill in the abyss with walls (ugly, need to optimize)'''
        for room in rooms:
            for direction in self.possible_directions(room):
                room.connections[direction] = { 'door': Wall() }

    def connect_randomly(self, origin, destination):
        '''Connect a room (origin) to a destination room in some random direction'''
        directions = self.possible_directions(destination)
        if not any(directions): return

        connect_dir = random.choice(directions)
        origin.coestablish_connection(connect_dir, destination)

    def possible_directions(self, room):
        '''Get all directions for a room that are not already specified'''
        return [d for d in room.connections if room.connections[d] is None]
