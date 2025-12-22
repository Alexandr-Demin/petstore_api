from httpx import Response
from clients.private_hhtps_bilder import get_private_https_client
from tools.routes import APIRoutes
from clients.api_client import APIClient


class PrivatePetClient(APIClient):
 
    def delete_pet_api(self, pet_id: int) -> Response:
        """
        Метод удаления питомца.
        
        :param request: ID питомца.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.delete(f'{APIRoutes.PET}/{pet_id}')
    
def get_private_user_client() -> PrivatePetClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """

    return PrivatePetClient(client=get_private_https_client())