from dependencies.app_initializer import app

from routes.v1.api import (
    news_collection_api,
    docs_api,
)

app.include_router(
    news_collection_api.get_public_router(), prefix="/api"
)

app.include_router(docs_api.get_public_router(), prefix="/api")
