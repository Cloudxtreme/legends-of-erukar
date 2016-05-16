from pynarpg.node.Interface import Interface
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

    def test_received_whisper(self):
        i = Interface()
        msg = {'message': 'inspect self', 'sender': {'uid': 'asdf'}}

        result = i.received_whisper(msg)

        self.assertIsNotNone(result)
        self.assertEqual(result.sender_uid, 'asdf')
