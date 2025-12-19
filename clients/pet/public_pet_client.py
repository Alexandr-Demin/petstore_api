from clients.api_client import APIClient
from clients.public_https_builder import get_public_https_client
from tools.routes import APIRoutes
from httpx import Response
from clients.pet.pet_schema import CreatePetRequestSchema, UpdateRequestSchema

class PublicPetClient(APIClient):

    def create_pet_api(self, request: CreatePetRequestSchema) -> Response:
        """
        Метод добавления питомца.
        
        :param request: Словарь с телом запроса для добавления питомцая.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.post(APIRoutes.PET, json=request.model_dump(by_alias=True))
    
    def update_existing_pet_api(self, request: UpdateRequestSchema) -> Response:
        """
        Метод обновление существующего питомца.
        
        :param request: Словарь с телом запроса для обновление питомцая.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.put(APIRoutes.PET, json=request.model_dump(by_alias=True))
   

def get_publick_users_client() -> PublicPetClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return PublicPetClient(client=get_public_https_client())