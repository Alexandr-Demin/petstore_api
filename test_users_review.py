from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema, UpdateUserRequestSchema
from clients.users.users_client import UserClient
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from http import HTTPStatus

class TestUser:
    """
    Тесты для эндпоинта /v2/user
    """
    def test_create_user(self, user_client: UserClient):
        """
        Тест создание пользователя.

        """

        request = CreateUserRequestSchema()
        response = user_client.create_user_api(request)

        response_data = CreateUserResponseSchema.model_validate_json(response.text)
        validate_json_schema(response.json(), response_data.model_json_schema())

        assert_status_code(response.status_code, HTTPStatus.OK)

    def test_get_user(self, user_client: UserClient, fuction_user: UserFixture):
        """
        Тест создание и получение пользователя.

        """

        get_response = user_client.get_user_by_user_name_api(username=fuction_user.request.user_name)

    def test_update_user(
            self, 
            user_client: UserClient, 
            fuction_user: UserFixture
    ):
        """
        Тест создание и обновление пользователя.

        """

        update_request_schema = UpdateUserRequestSchema()

        response = user_client.update_user_api(

            fuction_user.request.user_name, 
            update_request_schema
    )

    def test_delete_user(
            
            self, 
            user_client: UserClient, 
            fuction_user: UserFixture
    ):
        """
        Тест создание, удаление и проверка пользователя после удаления.

        """
        delete_user_response = user_client.delete_user_api(fuction_user.request.user_name)
        get_user_response = user_client.get_user_by_user_name_api(fuction_user.user_name)

        

        
