from httpx import Client
from config import setting

def get_private_https_client() -> Client:
    """
    Функция создаёт приватный экземпляр httpx.Client с базовыми настройками.

    :return: Готовый к использованию объект httpx.Client.
    """
    return Client(
        base_url=setting.http_client.client_url,
        timeout=setting.http_client.timeout,
        headers=setting.http_client.headers
    )