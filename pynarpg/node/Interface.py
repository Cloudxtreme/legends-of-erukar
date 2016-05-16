from pynarpg.factories.FactoryBase import FactoryBase
from pynarpg.node.DataAccess import DataAccess

class Interface:
    command_location = 'pynarpg.commands'

    def __init__(self):
        self.data = DataAccess()
        self.factory = FactoryBase()

    def received_whisper(self, whisper_msg):
        '''received_whisper hook for whenever the node gets a whisper message'''
        # Process the message to get everything you need to generate
        uid = whisper_msg['sender']['uid']
        command, payload = self.command_and_payload(whisper_msg['message'])
        target_command = '{0}.{1}'.format(Interface.command_location, command.capitalize())
        generation_parameters = { \
            'sender_uid': uid, \
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
