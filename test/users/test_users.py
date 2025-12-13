from clients.users.user_schema import CreateUserRequestSchema, UpdateUserRequestSchema
from clients.users.users_client import get_publick_users_client 


class TestUser:
    def test_create_user(self):
        request_data = CreateUserRequestSchema()
        client = get_publick_users_client()
        
        response = client.create_user_api(request_data)
        
        print(f"Ответ от API: {response}")
        print(f"Статус код: {response.status_code}")
        print(f"Тело ответа: {response.text}")

    def test_get_user(self):
        create_request_data = CreateUserRequestSchema()
        print(f"Тело запроса: {create_request_data}")
        create_user_client = get_publick_users_client()
        create_response = create_user_client.create_user_api(create_request_data)
        get_response = create_user_client.get_user_by_user_name_api(username=create_request_data.user_name)
        print(f"Статус код: {get_response.status_code}")
        print(f"Тело ответа: {get_response.text}")

    def test_update_user(self):
        create_request_data = CreateUserRequestSchema()
        update_request_data = UpdateUserRequestSchema()
        print(f"Тело запроса: {create_request_data}")
        print(f"Тело запроса для апдейта: {update_request_data}")
        create_user_client = get_publick_users_client()
        create_response = create_user_client.create_user_api(create_request_data)
        update_user = create_user_client.update_user_api(
            username=create_request_data.user_name,
            request=update_request_data
        )
        print(f"Статус код: {update_user.status_code}")
        print(f"Тело ответа: {update_user.text}")

    def test_delete_user(self):
        create_request_data = CreateUserRequestSchema()
        print(f"Тело запроса: {create_request_data}")
        create_user_client = get_publick_users_client()
        create_response = create_user_client.create_user_api(create_request_data)
        print(f"Статус код: {create_response.status_code}")
        print(f"Тело ответа: {create_response.text}")
        delete_user_request = create_user_client.delete_user_api(username=create_request_data.user_name)
        print(f"Статус код: {delete_user_request.status_code}")
        print(f"Тело ответа: {delete_user_request.text}")

