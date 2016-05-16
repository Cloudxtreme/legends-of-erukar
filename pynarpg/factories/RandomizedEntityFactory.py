from pynarpg.factories.FactoryBase import FactoryBase
import random

class RandomizedEntityFactory(FactoryBase):
    def generate(self, type_to_generate, yield_number, generation_parameters):
        '''Generates a certain number of elements'''
        return [self.create_one(type_to_generate, generation_parameters) \
            for x in range(0, yield_number)]

    def create_one(self, type_to_generate, generation_parameters):
        '''
        Create an object using generation_parameters to specify some sort of
        stochasticity in generation. For instance, you may pass in
        {'value': range(0,10)} to allow the generator to specify that the
        resultant object.value is any number in that specified range.
        '''
        shell = self.create_template(type_to_generate)
        for param in [x for x in generation_parameters if hasattr(shell, x)]:
            setattr(shell, param, random.choice(generation_parameters[param]))
        return shell
