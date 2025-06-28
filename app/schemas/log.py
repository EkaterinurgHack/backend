from pydantic import BaseModel, ConfigDict

class LogRecord(BaseModel):
    name: str
    message: str
    when: str

    model_config = ConfigDict(from_attributes=True)