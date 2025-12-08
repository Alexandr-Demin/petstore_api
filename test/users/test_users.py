from clients.users.user_schema import CreateUserRequestSchema
from clients.users.users_client import get_publick_users_client


class TestUser:
    def test_create_user(self):
        request_data = CreateUserRequestSchema()
        client = get_publick_users_client()
        
        # Вызываем API метод
        response = client.create_user_api(request_data)
        
        print(f"Ответ от API: {response}")
        print(f"Статус код: {response.status_code}")
        print(f"Тело ответа: {response.text}")