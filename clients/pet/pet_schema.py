from pydantic import BaseModel, ConfigDict, Field
from tools.fakers import fake

class Category(BaseModel):
    
    id: int=Field(default_factory=fake.integer)
    name: str=Field(default_factory=fake.pet_name)

class Tags(BaseModel):

    id: int=Field(default_factory=fake.integer)
    name: str=Field(default_factory=fake.sentence)

class CreatePetRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int | None=Field(default_factory=fake.integer)
    category: Category 
    name: str=Field(default_factory=fake.first_name)
    photo_urls: list[str]=Field(alias='photoUrls',default_factory=fake.image_url)
    tags: list[Tags]
    status: str | None=Field(default_factory=fake.pet_status)

class CreatePetResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int=Field(default_factory=fake.integer)
    category: Category
    name: str=Field(default_factory=fake.first_name)
    photo_urls: list[str]=Field(alias='photoUrls',default_factory=fake.image_url)
    tags: list[Tags]
    status: str | None=Field(default_factory=fake.pet_status)

class UpdateRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int=Field(default_factory=fake.integer)
    category: Category
    name: str=Field(default_factory=fake.first_name)
    photo_urls: list[str]=Field(alias='photoUrls',default_factory=fake.image_url)
    tags: list[Tags]
    status: str=Field(default_factory=fake.pet_status)

class UpdateResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int=Field(default_factory=fake.integer)
    category: Category
    name: str=Field(default_factory=fake.first_name)
    photo_urls: list[str]=Field(alias='photoUrls',default_factory=fake.image_url)
    tags: list[Tags]
    status: str=Field(default_factory=fake.pet_status)