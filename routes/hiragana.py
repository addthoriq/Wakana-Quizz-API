from fastapi import APIRouter
from src.hiragana import hira_std, hira_tenmaru, hira_yoon, hiraganas
import random

router: APIRouter = APIRouter(prefix="/hiragana", tags=["Hiragana Letter's"])

hiraKey = None


# Generate Hiragana
def generate_hiragana(data: dict[str, str]) -> tuple[str, str]:
    hiraKey, hiraVal = random.choice(list(data.items()))
    return hiraKey, hiraVal


@router.get("/")
async def get_all_hiragana():
    return hiraganas


@router.get("/standart")
async def get_hiragana_standart():
    return hira_std


@router.get("/tenten-maru")
async def get_hiragana_tenten_maru():
    return hira_tenmaru


@router.get("/yoon")
async def get_hiragana_yoon():
    return hira_yoon
