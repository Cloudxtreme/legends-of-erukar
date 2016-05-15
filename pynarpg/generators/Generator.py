from pynarpg.model.RpgEntity import RpgEntity
import random

class Generator(RpgEntity):
    def __init__(self, type_to_generate):
        split_results = type_to_generate.split('.')
        self.module_name = '.'.join(split_results[:-1])
        self.type_to_generate = split_results[-1]
        self.module = __import__(self.module_name)

    def generate(self, yield_number, generation_parameters):
        '''Generates a certain number of elements'''
        return [self.create_one(generation_parameters) for x in range(0,yield_number)]

    def create_template(self):
        '''Create a blank template'''
        if not hasattr(self.module, self.type_to_generate):
            return
        return getattr(self.module, self.type_to_generate)()

    def create_one(self, generation_parameters):
        '''
        Create an object using generation_parameters to specify some sort of
        stochasticity in generation. For instance, you may pass in
        {'value': range(0,10)} to allow the generator to specify that the
        resultant object.value is any number in that specified range.
        '''
        shell = self.create_template()
        for param in [x for x in generation_parameters if hasattr(shell, x)]:
            setattr(shell, param, random.choice(generation_parameters[param]))
        return shell
