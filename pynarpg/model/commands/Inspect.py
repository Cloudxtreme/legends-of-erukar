from pynarpg.model.Command import Command

class Inspect(Command):
    def __init__(self):
        super().__init__()

    def execute(self, contents):
        if 'self' in contents:
            return 'This is you'
        return 'This is another person'
