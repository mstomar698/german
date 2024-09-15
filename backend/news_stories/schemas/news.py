
from pydantic import BaseModel # type: ignore
from typing import Optional, List


class NewsItem(BaseModel):
    id: int
    by: Optional[str] = None
    descendants: Optional[int] = None
    kids: Optional[List[int]] = None
    score: Optional[int] = None
    time: Optional[int] = None
    title: Optional[str] = None
    type: Optional[str] = None
    url: Optional[str] = None

    class Config:
        orm_mode = True
