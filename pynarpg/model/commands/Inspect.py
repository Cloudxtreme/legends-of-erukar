from pynarpg.model.Command import Command

class Inspect(Command):
    def __init__(self):
        super().__init__()

    def execute(self, contents):
        return contents
