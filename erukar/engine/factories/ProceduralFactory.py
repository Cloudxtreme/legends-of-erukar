from . import FactoryBase

class ProceduralFactory(FactoryBase):
    def generate(self):
        '''
        Here, the programmer specifies a distribution that is relevant.
        Examples:
        numpy.random.gamma(7.5, 1.0)
        '''
        return
