from erukar.engine.model.RpgEntity import RpgEntity
import random

class EntityLocation(RpgEntity):
    description_types = [
        'there {0} {1} {2} {3} {4}',
        '{3} {4} {0} {1} {2}',
        '{3} {4} there {0} {1} {2}',
        '{3} {4} of this room there {0} {1} {2}'
    ]

    def __init__(self, entity, article, preposition, plural=False):
        self.entity = entity
        self.article = article
        self.preposition = preposition
        self.plural = plural

    def describe(self, origin=''):
        chosen = random.choice(EntityLocation.description_types)
        return ' '.join(chosen.format(self.plurality(), self.article, self.entity.get_name(), self.preposition, origin).split()).capitalize() + '.'

    def plurality(self):
        if self.plural:
            return 'are'
        return 'is'

    def matches(self, other):
        return self.entity.matches(other)

    def on_inspect(self, other):
        return self.entity.on_inspect(other)

    def get_name(self):
        return self.entity.get_name()

    def take_damage(self, damage):
        return self.entity.take_damage(damage)

    def calculate_armor_class(self):
        if hasattr(self.entity, 'calculate_armor_class'):
            return getattr(self.entity, 'calculate_armor_class')()

        return 5

    def on_open(self, sender):
        return self.entity.on_open(sender)

    def on_close(self, sender):
        return self.entity.on_close(sender)
