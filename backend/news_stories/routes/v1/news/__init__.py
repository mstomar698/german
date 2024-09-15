from fastapi import APIRouter # type: ignore


def get_public_router():
    router: APIRouter = APIRouter()
    router.tags = ["public"]
    return router

