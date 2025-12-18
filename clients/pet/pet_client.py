from clients.api_client import APIClient
from tools.routes import APIRoutes
from httpx import Response
from clients.pet.pet_schema import CreatePetRequestSchema

class PetClient(APIClient):

    def create_pet_api(self, request: CreatePetRequestSchema) -> Response:
        """
        Метод добавления питомца.
        
        :param request: Словарь с телом запроса для добавления питомцая.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.post(APIRoutes.PET, json=request.model_dump())