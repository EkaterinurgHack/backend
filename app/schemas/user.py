from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

class UserInfo(BaseModel):
    user_id: int
    nickname: str

    model_config = ConfigDict(from_attributes=True, alias_generator=to_camel, populate_by_name=True)