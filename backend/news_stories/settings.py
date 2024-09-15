import os
from dotenv import load_dotenv # type: ignore
import pytz # type: ignore

load_dotenv()

REDIS_CONFIG = {
    "host": os.getenv("REDIS_HOST", "localhost"),
    "port": os.getenv("REDIS_PORT", 6379),
    "db": os.getenv("REDIS_DB", 0),
}

SECRET_KEY = os.getenv("SECRET_KEY")

INTERNAL_COMMUNICATION_SECRET = os.getenv(
    "INTERNAL_COMMUNICATION_SECRET", "string"
)

CACHE_EXPIRY = os.getenv("CACHE_EXPIRY", 60)

INTERNAL_COMMUNICATION_URL = os.getenv(
    "INTERNAL_COMMUNICATION_URL", "http://localhost:8000"
)

HACKER_NEWS_TOP_STORIES_URL = os.getenv(
    "HACKER_NEWS_TOP_STORIES_URL", "https://hacker-news.firebaseio.com/v0/topstories.json"
)

HACKER_NEWS_ITEM_URL = os.getenv(
    "HACKER_NEWS_ITEM_URL", "https://hacker-news.firebaseio.com/v0/item/{}.json"
)

IST_TIMEZONE = pytz.timezone("Asia/Kolkata")
