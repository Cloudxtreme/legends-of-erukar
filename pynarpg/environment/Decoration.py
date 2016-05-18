from pynarpg.model.EnvironmentPiece import EnvironmentPiece

class Decoration(EnvironmentPiece):
    def __init__(self, aliases, results):
        super().__init__()
        self.aliases = aliases
        self.inspect_results = results

    def on_inspect(self):
        return self.inspect_results

    def matches(self, query):
        return any([query in alias for alias in self.aliases])
