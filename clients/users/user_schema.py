from pydantic import BaseModel, ConfigDict, Field
from tools.fakers import fake


class CreateUserRequestSchema(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    id: int | None=Field(default_factory=fake.integer)
    user_name: str | None=Field(alias="username", default_factory=fake.user_name)
    first_name: str | None=Field(alias="firstName", default_factory=fake.first_name)
    last_name: str | None=Field(alias="lastName", default_factory=fake.last_name)
    email: str | None=Field(default_factory=fake.email)
    password: str | None=Field(default_factory=fake.password)
    phone: str | None=Field(default_factory=fake.phone)
    user_status: int | None=Field(alias="userStatus", default_factory=fake.user_status)

class CreateUserResponseSchema(BaseModel):
    
    code: int
    type: str
    message: str