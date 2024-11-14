from fastapi import APIRouter
from schemas.hiragana import CheckHiragana
import random
import json

router: APIRouter = APIRouter(prefix="/hiragana", tags=["Hiragana"])

hiraKey = None

# Generate Hiragana
def generate_hiragana() -> tuple[str, str]:
    f = open("./src/hiragana.json")
    data = json.load(f)
    hiraKey, hiraVal = random.choice(list(data.items()))
    return hiraKey, hiraVal


@router.get("/")
async def get_hiragana() -> str:
    global hiraKey
    hiraKey, hiraVal = generate_hiragana()
    return hiraVal


@router.post("/")
async def check_hiragana(input: CheckHiragana) -> bool:
    global hiraKey
    input_hira = input.key_input
    if input_hira == hiraKey:
        return True
    else:
        return False
