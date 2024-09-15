
import secrets 
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html # type: ignore
from fastapi.openapi.utils import get_openapi # type: ignore
from fastapi import Depends, HTTPException, status # type: ignore
from fastapi.security import HTTPBasic, HTTPBasicCredentials # type: ignore
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html # type: ignore

from . import get_public_router
from dependencies.app_initializer import app

public_router = get_public_router()


security = HTTPBasic()


def get_current_username(
    credentials: HTTPBasicCredentials = Depends(security),
):
    correct_username = secrets.compare_digest(credentials.username, "user")
    correct_password = secrets.compare_digest(credentials.password, "password")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@public_router.get("/redoc", include_in_schema=False)
async def get_redoc_documentation(
    username: str = Depends(get_current_username),
):
    return get_redoc_html(openapi_url="/api/openapi.json", title="docs")


@public_router.get("/docs", include_in_schema=False)
async def get_documentation(username: str = Depends(get_current_username)):
    return get_swagger_ui_html(openapi_url="/api/openapi.json", title="docs")


@public_router.get("/openapi.json", include_in_schema=False)
async def openapi(username: str = Depends(get_current_username)):
    return get_openapi(title=app.title, version=app.version, routes=app.routes)
