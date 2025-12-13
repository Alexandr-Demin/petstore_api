from httpx import Response
from clients.api_client import APIClient
from clients.public_https_builder import get_public_https_client
from clients.users.user_schema import CreateUserRequestSchema, UpdateUserRequestSchema
from tools.routes import APIRoutes


class UserClient(APIClient):
    """
    Клиент для работы с /v2/user
    """
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Метод создания пользователя.
        
        :param request: Словарь с телом запроса для создания пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.post(APIRoutes.USER, json=request.model_dump(by_alias=True))
    
    def get_user_by_user_name_api(self, username: str) -> Response:
        """
        Метод получения пользователя по имени.
        
        :param username: Имя пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get(f'{APIRoutes.USER}/{username}')
    
    def update_user_api(self, username: str, request: UpdateUserRequestSchema) ->Response:
        """
        Метод обновления пользователя по имени.
        
        :param username: Имя пользователя.
        :param request: Словарь с телом запроса для обновления пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.put(f'{APIRoutes.USER}/{username}', json=request.model_dump(by_alias=True))
    
    def delete_user_api(self, username: str) -> Response:
        """
        Метод удаления пользователя по имени.
        
        :param username: Имя пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.delete(f'{APIRoutes.USER}/{username}')
    
def get_publick_users_client() -> UserClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return UserClient(client=get_public_https_client())