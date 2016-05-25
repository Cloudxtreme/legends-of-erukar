from pynarpg import *
import unittest

class InterfaceTests(unittest.TestCase):
    def test_command_and_payload_no_word(self):
        i = Interface()

        method, contents = i.command_and_payload('inspect')

        self.assertEqual(method, 'inspect')
        self.assertEqual(contents, '')

    def test_command_and_payload_single_word(self):
        i = Interface()

        method, contents = i.command_and_payload('inspect other')

        self.assertEqual(method, 'inspect')
        self.assertEqual(contents, 'other')
