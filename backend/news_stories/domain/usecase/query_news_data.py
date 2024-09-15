
import json
from dependencies.redis_initializer import get_redis_client
from settings import CACHE_EXPIRY, HACKER_NEWS_ITEM_URL
import httpx  # type: ignore
from fastapi import HTTPException, status # type: ignore
import asyncio
import logging

logger = logging.getLogger(__name__)

async def fetch_story(client: httpx.AsyncClient, story_id: int):
    """
    Helper function to fetch a single story by ID.
    """
    cache_key = f"story:{story_id}"

    try:
        redis_client = get_redis_client()
    except Exception as e:
        logger.error(f"Redis connection error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Failed to connect to Redis"
        )

    try:
        cached_story = redis_client.get(cache_key)
        if cached_story:
            story = json.loads(cached_story)
            return story
    except Exception as e:
        logger.error(f"Redis get error: {str(e)}")

    try:
        response = await client.get(HACKER_NEWS_ITEM_URL.format(story_id), timeout=10.0)
        response.raise_for_status()
        story = response.json()

        if not story or story.get('deleted') or story.get('dead'):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Story with ID {story_id} not found or is unavailable."
            )
    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Error fetching story with ID {story_id}: {e.response.text}"
        )
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Network error while fetching story with ID {story_id}: {str(e)}"
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error parsing JSON for story with ID {story_id}: {str(e)}"
        )

    try:
        redis_client.setex(cache_key, CACHE_EXPIRY, json.dumps(story))
    except Exception as e:
        logger.error(f"Redis set error: {str(e)}")

    return story
