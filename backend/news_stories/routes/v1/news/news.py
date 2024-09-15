
from settings import HACKER_NEWS_TOP_STORIES_URL
from . import get_public_router
from domain.usecase.query_news_data import fetch_story
from schemas.news import NewsItem
from typing import List
import httpx # type: ignore
import asyncio
from fastapi import HTTPException, status # type: ignore

public_router = get_public_router()

@public_router.get("/health-check")
def health_check():
    return {"status": "ok"}

@public_router.get("/get-news", response_model=List[NewsItem])
async def get_top_stories():
    """
    Fetch the top 10 stories from Hacker News and return them as a list.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(HACKER_NEWS_TOP_STORIES_URL, timeout=10.0)
            response.raise_for_status()
            top_stories_ids = response.json()[:10]

            tasks = [
                fetch_story(client, story_id)
                for story_id in top_stories_ids
            ]

            stories = await asyncio.gather(*tasks)
        return stories
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching stories: {str(e)}"
        )

@public_router.get("/get-news/{id}", response_model=NewsItem)
async def get_story_by_id(id: int):
    """
    Fetch a single news item by its ID.
    """
    try:
        async with httpx.AsyncClient() as client:
            story = await fetch_story(client, id)
        return story
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching story with ID {id}: {str(e)}"
        )