from pydantic import BaseModel


class Url(BaseModel):
    product: str
    url: str
