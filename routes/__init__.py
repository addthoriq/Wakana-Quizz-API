from fastapi import APIRouter
from .hiragana import router as hira_router

routers: APIRouter = APIRouter()

routers.include_router(hira_router)
