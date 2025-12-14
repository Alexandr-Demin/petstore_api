from pydantic import BaseModel
import pytest
from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema
from clients.users.users_client import UserClient, get_publick_users_client

class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def user_name(self) ->str:
        return self.request.user_name


@pytest.fixture
def user_client() -> UserClient:
    return get_publick_users_client()

@pytest.fixture
def fuction_user(user_client: UserClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = user_client.create_user(request)
    return UserFixture(request=request, response=response)