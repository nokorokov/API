from pydantic import BaseModel, Field


class Post(BaseModel):
    id: int = Field(le=2)
    title: str


## {'id': 1, 'title': 'Post 1'}
