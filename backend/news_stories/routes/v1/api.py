
from routes.v1.news.news import (
    public_router as data_pub_ro,
)

from routes.v1.generic.docs import (
    public_router as docs_pub_ro,
)

from fastapi import APIRouter # type: ignore

from routes.api import APIRouter

    
class NewsApi(APIRouter):
    def __init__(self, public_router):
        super().__init__(public_router, public_router)
    
    def get_public_router(self):
        return self.public_router
    
    def get_private_router(self):
        return


class DocsApi(APIRouter):
    def __init__(self, public_router):
        super().__init__(public_router, public_router)

    def get_public_router(self):
        return self.public_router

    def get_private_router(self):
        return


news_collection_api = NewsApi(data_pub_ro)
docs_api = DocsApi(docs_pub_ro) 
