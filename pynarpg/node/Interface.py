from pynarpg.factories.FactoryBase import FactoryBase
from pynarpg.node.DataAccess import DataAccess
from pynarpg.environment import *
from pynarpg.lifeforms.Player import Player
from pynarpg.model.PlayerNode import PlayerNode

class Interface:
    command_location = 'pynarpg.commands'

    def __init__(self):
        self.data = DataAccess()
        self.factory = FactoryBase()

    def received_whisper(self, whisper_msg):
        '''received_whisper hook for whenever the node gets a whisper message'''
        # Process the message to get everything you need to generate
        uid = whisper_msg['sender']['uid']
        line = whisper_msg['message']

        return self.execute(uid, line)

    def execute(self, uid, line):
        command, payload = self.command_and_payload(line)
        target_command = '{0}.{1}'.format(Interface.command_location, command.capitalize())
        generation_parameters = {
            'sender_uid': uid,
            'data': self.data }

        # Now actually make the thing with specified params
        created = self.factory.create_one(target_command, generation_parameters)

        # The Command tcan return something if it needs to for some reason
        return created.execute(payload)


    def command_and_payload(self, message):
        '''
        Split the received chat message into the first word (will be used to
        create the command object) and the remaining data, which will be used
        as the payload into the instantiated object
        '''
        out = message.split(' ', 1)
        return [out[i] if i < len(out) else '' for i in [0, 1]]

    def run_command_line(self):
        p = Player()
        p.uid = 'Bob'

        self.data.players.append(PlayerNode(p.uid, p))

        n = Room()
        n.description = 'This is the North Room'

        c = Room()
        c.description = 'This is the central area'

        s = Room()
        n.description = 'This is the South Room'

        d = Door()
        c.coestablish_connection(Room.North, n, None)
        c.coestablish_connection(Room.South, s, d)
        p.current_room = n

        while True:
            line = input('> ')
            res = self.execute(p.uid, line)
            print(res)
