from clients.users.user_schema import CreateUserRequestSchema
from clients.users.users_client import get_publick_users_client


class TestUser:
    def test_create_user(self, request: CreateUserRequestSchema):
        request = get_publick_users_client.cre