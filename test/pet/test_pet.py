from clients.pet.pet_schema import CreatePetRequestSchema, CreatePetResponseSchema
from clients.pet.public_pet_client import PublicPetClient
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from http import HTTPStatus


class TestPet:
    """
    Тесты для эндпоинта /v2/pet
    """

    def test_create_pet(self, pet_client: PublicPetClient):
        """
        Тест создание питомца.

        """
        request = CreatePetRequestSchema()
        response = pet_client.create_pet_api(request)
        response_data = CreatePetResponseSchema.model_validate_json(response.text)

        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_status_code(response.status_code, HTTPStatus.OK)

