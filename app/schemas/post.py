from typing import List
from datetime import datetime
import uuid

from app.schemas.image import ImageRead
from sqlmodel import Field, SQLModel
from app.schemas.comment import CommentRead
from app.schemas.like import LikeRead


class PostCreate(SQLModel):
    description: str
    user_id: uuid.UUID


class PostRead(SQLModel):
    id: uuid.UUID
    user_id: uuid.UUID
    description: str
    created_at: datetime
    likes_count: int = 0
    comments_count: int = 0


class PostReadDetails(SQLModel):
    id: uuid.UUID
    user_id: uuid.UUID
    description: str
    created_at: datetime
    images: List[ImageRead] = Field(default_factory=list)
    likes: List[LikeRead] = Field(default_factory=list)
    comments: List[CommentRead] = Field(default_factory=list)


class PostUpdate(SQLModel):
    description: str | None = None
    user_id: uuid.UUID | None = None