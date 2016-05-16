from pynarpg.factories.FactoryBase import FactoryBase
from pynarpg.node.DataAccess import DataAccess

class Interface:
    command_location = 'pynarpg.model.commands'

    def __init__(self):
        self.data = DataAccess()
        self.factory = FactoryBase()

    def received_whisper(self, whisper_msg):
        uid = whisper_msg['sender']['uid']
        command, payload = self.command_and_payload(whisper_msg['message'])
        target_command = '{0}.{1}'.format(Interface.command_location, command.capitalize())
        return self.factory.create_one(target_command, {'sender_uid': uid})

    def command_and_payload(self, message):
        '''
        Split the received chat message into the first word (will be used to
        create the command object) and the remaining data, which will be used
        as the payload into the instantiated object
        '''
        out = message.split(' ', 1)
        return [out[i] if i < len(out) else '' for i in [0, 1]]
