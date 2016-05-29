from erukar.engine.factories.FactoryBase import FactoryBase
from erukar.engine.environment import *
from erukar.engine.model import Direction
import numpy as np
import math, random

class DungeonGenerator(FactoryBase):
    minimum_rooms = 3
    def __init__(self):
        self.dungeon_map = {}

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

    def map_to_string(self):
        maxes = [max([m[i] for m in self.dungeon_map]) for i in range(2)]
        mins = [min([m[i] for m in self.dungeon_map]) for i in range(2)]

        # This really should be cleaned up
        result_str = ''
        for y in range(mins[1], maxes[1]+1):
            new_row = ''
            for x in range(mins[0], maxes[0]+1):
                if (x,y) in self.dungeon_map:
                    if (x,y) == (0,0):
                        new_row += 'O'
                    else:
                        new_row += '#'
                else:
                    new_row += ' '
            result_str = new_row + '\n' + result_str
        return result_str

    def connect_rooms(self, rooms):
        '''Connect a list of rooms to each other'''
        self.dungeon_map[(0,0)] = rooms[0]
        rooms[0].coordinates = (0,0)
        self.connect_randomly(rooms[0], rooms[1])


        while any(self.unconnected(rooms)):
            print(len(self.unconnected(rooms)))
            origin_room = random.choice(self.connected(rooms))
            next_room = random.choice(self.unconnected(rooms))
            self.connect_randomly(origin_room, next_room)

    def connected(self, rooms):
        return [r for r in rooms if len(self.possible_directions(r)) < 4]

    def unconnected(self, rooms):
        return [r for r in rooms if len(self.possible_directions(r)) == 4]

    def generate_descriptions(self, rooms):
        ''' Add descriptions '''
        for r,i in zip(rooms, range(len(rooms))):
            r.description = 'This is the {0}th room at ({1}, {2}).'.format(i, *r.coordinates)

    def fill_walls(self, rooms):
        '''Fill in the abyss with walls (ugly, need to optimize)'''
        for room in rooms:
            for direction in self.possible_directions(room):
                room.connections[direction] = { 'door': Wall() }

    def connect_randomly(self, origin, destination):
        '''Connect a room (origin) to a destination room in some random direction'''
        directions = self.possible_directions(destination)
        if not any(directions): return

        direction = random.choice(directions)
        new_coords = self.to_coordinate(origin.coordinates, direction)
        if new_coords in self.dungeon_map:
            destination = self.dungeon_map[new_coords]

        origin.coestablish_connection(direction, destination)
        destination.coordinates = self.to_coordinate(origin.coordinates, direction)
        self.dungeon_map[(destination.coordinates)] = destination


    def possible_directions(self, room):
        '''Get all directions for a room that are not already specified'''
        return [d for d in room.connections if room.connections[d] is None]

    def number_of_connections(self):
        return math.ceil(math.sqrt(random.uniform(0, 1)*10))-1

    def to_coordinate(self, origin_coord, direction):
        '''Hmm, how do I clean this up?'''
        if direction is Direction.North:
            return (origin_coord[0], origin_coord[1]+1)
        if direction is Direction.East:
            return (origin_coord[0]+1, origin_coord[1])
        if direction is Direction.South:
            return (origin_coord[0], origin_coord[1]-1)
        if direction is Direction.West:
            return (origin_coord[0]-1, origin_coord[1])
        # Otherwise, just return the origin point... used when first generating
        return (0, 0)
