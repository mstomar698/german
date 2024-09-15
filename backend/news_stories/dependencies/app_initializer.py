
import os
from starlette.templating import Jinja2Templates # type: ignore
from fastapi import FastAPI # type: ignore
from fastapi_utils.tasks import repeat_every # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore

app = FastAPI()

templates = Jinja2Templates(
    directory=os.path.abspath(os.path.expanduser("templates"))
)


origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
@repeat_every(seconds=60)  # 1 minute
async def periodic_task():
    print(1, 'The task is running every minute')