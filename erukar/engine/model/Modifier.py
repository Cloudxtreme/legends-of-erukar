class Modifier:
    '''Used to alter any RpgEntity'''
    NONE = 0
    NONE_PROHIBITED = 1
    ALL_PERMITTED = 2
    ALL = 3

    def __init__(self):
        '''Allows explicit permission and explicit prohibition'''
        self.permitted_entities = []
        self.prohibited_entities = []
        self.permission_type = Modifier.ALL

    def modify(self, entity):
        '''Safe-guarded modification entry point'''
        if self.can_apply_to(entity):
            self.apply_to(entity)

    def apply_to(self, entity):
        '''Actually does the modification; this should be overridden'''
        pass

    def can_apply_to(self, entity):
        '''
        Checks to see if this is a valid entity based on entities specified
        in permitted_entities and prohibited_entities and this Modifier's
        permission_type
        '''
        if self.permission_type is Modifier.NONE_PROHIBITED:
            return not any(r for r in self.prohibited_entities if r == type(entity))

        if self.permission_type is Modifier.ALL_PERMITTED:
            return self.is_in_group(entity, self.permitted_entities)

        return self.permission_type is Modifier.ALL

    def is_in_group(self, entity, group):
        return any(r for r in group if r == type(entity) or issubclass(type(entity), r))
