from pydantic import BaseModel


class SocialMediaPostRequest(BaseModel):
    product: str
    platform: str
