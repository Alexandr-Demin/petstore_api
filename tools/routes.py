from enum import Enum

class APIRoutes(str, Enum):
    USER = '/v2/user'

    def __str__(self):
        return self.value