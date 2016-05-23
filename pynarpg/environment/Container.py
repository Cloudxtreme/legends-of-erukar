from pynarpg import RpgEntity

class Container(RpgEntity):
    def on_open(self, sender):
        return "Opened a chest"

    def on_close(self, sender):
        return "Closed a chest"

    def matches(self, other):
        return other.lower() == 'chest'
