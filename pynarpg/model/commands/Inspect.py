from pynarpg.model.Command import Command

class Inspect(Command):
    def __init__(self):
        pass

    def execute(self, contents):
        print(contents)
