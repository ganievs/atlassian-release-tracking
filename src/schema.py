from pydantic import BaseModel


class Application(BaseModel):
    name: str
    version: str
    class Config:
        orm_mode = True

