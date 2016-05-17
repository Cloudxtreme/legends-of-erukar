from pynarpg.model.EnvironmentPiece import EnvironmentPiece

class Chest(EnvironmentPiece):
    def on_open(self, sender):
        return "Opened a chest"

    def matches(self, other):
        return other.lower() == 'chest'
