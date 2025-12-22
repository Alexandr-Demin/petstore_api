from pydantic import BaseModel
import pytest
from clients.pet.pet_schema import CreatePetRequestSchema, CreatePetResponseSchema
from clients.pet.public_pet_client import PublicPetClient, get_publick_users_client


class PetFixture(BaseModel):
    request: CreatePetRequestSchema
    response: CreatePetResponseSchema

@pytest.fixture
def pet_client() ->PublicPetClient:
    return get_publick_users_client()

@pytest.fixture
def function_pet(user_client: PublicPetClient) -> PetFixture:
    request = CreatePetRequestSchema()
    response = user_client.create_pet_api(request)
    return PetFixture(request=request, response=response)