from httpx import Response
from clients.api_client import APIClient
from clients.public_https_builder import get_public_https_client
from clients.users.user_schema import CreateUserRequestSchema
from tools.routes import APIRoutes


class UserClient(APIClient):

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:

        return self.post(APIRoutes.USER, json=request.model_dump(by_alias=True))
    
def get_publick_users_client() -> UserClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return UserClient(client=get_public_https_client())