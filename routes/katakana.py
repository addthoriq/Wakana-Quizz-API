from fastapi import APIRouter
from src.katakana import kata_std, kata_tenmaru, kata_yoon, katakanas
import random

router: APIRouter = APIRouter(prefix="/katakana", tags=["Katakana Letter's"])

kataKey = None


# Generate Hiragana
def generate_katakana(data: dict[str, str]) -> tuple[str, str]:
    kataKey, kataVal = random.choice(list(data.items()))
    return kataKey, kataVal


@router.get("/")
async def get_all_katakana():
    return katakanas


@router.get("/standart")
async def get_katakana_standart():
    return kata_std


@router.get("/tenten-maru")
async def get_katakana_tenten_maru():
    return kata_tenmaru


@router.get("/yoon")
async def get_katakana_yoon():
    return kata_yoon
