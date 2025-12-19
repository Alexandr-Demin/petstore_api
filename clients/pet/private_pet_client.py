from httpx import Response
from pydantic import BaseModel
from tools.routes import APIRoutes


class PrivatePetClient(BaseModel):
 
    def delete_pet_api(self, pet_id: int, headers: str) -> Response:

        return self.delete(f'{APIRoutes.PET}/{pet_id}', headers=headers)