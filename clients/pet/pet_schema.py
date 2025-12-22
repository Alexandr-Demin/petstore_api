from pydantic import BaseModel, ConfigDict, Field
from tools.fakers import fake

class Category(BaseModel):
    
    id: int=Field(default_factory=fake.integer)
    name: str=Field(default_factory=fake.pet_name)

class Tags(BaseModel):

    id: int=Field(default_factory=fake.integer)
    name: str=Field(default_factory=fake.sentence)

class PetSchema(BaseModel):
    """
    Cтруктуры запроса на создание питомца.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: int | None=Field(default_factory=fake.integer)
    category: Category=Field(default_factory=Category) 
    name: str=Field(default_factory=fake.first_name)
    photo_urls: list[str]=Field(alias='photoUrls',default_factory=lambda: [fake.image_url()])
    tags: list[Tags]=Field(default_factory=lambda: [Tags()])
    status: str | None=Field(default_factory=fake.pet_status)



class CreatePetRequestSchema(PetSchema):
    """
    Описание структуры запроса на создание питомца.
    """

    pass

class CreatePetResponseSchema(PetSchema):
    """
    Описание структуры ответа при создание питомца.
    """
    pass

class UpdateRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновлдение созданного питомца.
    """
    pass

class UpdateResponseSchema(BaseModel):
    """
    Описание структуры ответа на обновлдение созданного питомца.
    """
    pass