import datetime
from typing import Optional

from pydantic import BaseModel, Field


class UserGet(BaseModel):
    id: int
    age: int
    city: str
    country: str
    exp_group: int
    gender: int
    os: str
    source: str
    class Config:
        orm_mode = True


class PostGet(BaseModel):
    id: int
    text: str
    topic: str
    class Config:
        orm_mode = True


class FeedGet(BaseModel):
    user_id: int
    post_id: int
    user: UserGet
    post: PostGet
    action: str
    time: datetime.datetime

    class Config:
        orm_mode = True
