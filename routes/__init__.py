from fastapi import APIRouter
from .hiragana import router as hira_router
from .katakana import router as kata_router
from .all_letters import router as all_letter_router

routers: APIRouter = APIRouter()

routers.include_router(all_letter_router)
routers.include_router(hira_router)
routers.include_router(kata_router)
