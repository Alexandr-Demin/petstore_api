from enum import Enum

class APIRoutes(str, Enum):
    USER = '/v2/user'
    PET = '/v2/pet'
    STORE = '/v2/store'

    def __str__(self):
        return self.value