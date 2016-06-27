from erukar import *
import unittest

class ProbablisticGeneratorTests(unittest.TestCase):
    def test_create_distribution_should_make_weighted_bins(self):
        gen = ProbablisticGenerator()
        gen.create_distribution(['a', 'b'], [1, 1])

        self.assertTrue(all(f in [0.5, 1,0] for f in gen.bins))
