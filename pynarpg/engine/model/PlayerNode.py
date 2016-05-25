from pynarpg.engine.model.EntityLocation import EntityLocation

class PlayerNode:
    def __init__(self, uid, character):
        self.uid = uid
        self.character = character
        self.item_indexer = {}

    def index_item(self, item, container):
        '''Used to store to traverse paths through a container tree to find an object'''
        if type(item) is EntityLocation:
            item = item.entity
        if container not in self.item_indexer:
            self.item_indexer[container] = []
        self.item_indexer[item] = self.item_indexer[container] + [container]

    def index(self, item):
        '''Get a traverse path from the indexer (if it exists)'''
        if item in self.item_indexer:
            return self.item_indexer[item]
        return []

    def reverse_index(self, container):
        '''Get all contents of a container'''
        return [item for item in self.item_indexer if container in self.item_indexer[item]]

    def remove_index(self, item):
        if item in self.item_indexer:
            self.item_indexer.pop(item, None)
