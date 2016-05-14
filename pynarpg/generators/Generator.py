from pynarpg.model.RpgEntity import RpgEntity

class Generator(RpgEntity):
    def __init__(self, type_to_generate):
        split_results = type_to_generate.split('.')
        self.module_name = '.'.join(split_results[:-1])
        self.type_to_generate = split_results[-1]
        self.module = __import__(self.module_name)

    def generate(self, yield_number):
        '''Generates a certain number of elements'''
        self.create_one()

    def create_one(self):
        if not hasattr(self.module, self.type_to_generate):
            return
        return getattr(self.module, self.type_to_generate)()
