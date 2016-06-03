from . import FactoryBase

class StochasticGenerator(FactoryBase):
    def __init__(self, options=None):
        super().__init__()
        self.options_to_weights = options if options is not None else {}

    def generate(self):
        '''
        First create a density function according to each option's weight
        '''
        return
