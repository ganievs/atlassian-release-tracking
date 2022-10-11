from pydantic import BaseModel


class Url(BaseModel):
    product: str
    url: str

    class Config:
        schema_extra = {
            "example": {
                "product": "jira-core",
                "url": "https://raw.githubusercontent.com/ganievs/atlasian-release-tracking/main/data/jira-core.json",
            }
        }
