
import redis # type: ignore
from fastapi import HTTPException # type: ignore
from settings import REDIS_CONFIG
import logging

logger = logging.getLogger(__name__)

class RedisClient:
    def __init__(self, config):
        self.config = config
        self.client = None

    def __enter__(self):
        self.client = redis.StrictRedis(**self.config)
        return self.client

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.client:
            self.client.close()


def get_redis_client() -> redis.StrictRedis:
    try:
        return redis.StrictRedis(**REDIS_CONFIG)
    except Exception as e:
        logger.error(f"Error connecting to Redis: {str(e)}")
        raise HTTPException(
            status_code=500, detail="Failed to connect to Redis"
        )
