from fastapi import APIRouter, Depends
from src import hiragana, katakana
from schemas.all_letters import LettersAll, CheckLetters
import random
from typing import Any

router = APIRouter(prefix="/guess-letters", tags=["Guess the letters"])

lettersKey = None
lettersVal = None
score_hira = 0
score_kata = 0
score_hira_wrong = 0
score_kata_wrong = 0


# Generate Hiragana
def generate_lettersgana(data: dict[str, str]) -> tuple[str, str]:
    lettersKey, lettersVal = random.choice(list(data.items()))
    return lettersKey, lettersVal


@router.get("/")
async def guess_letters(params: LettersAll = Depends()) -> str:
    global lettersKey, lettersVal
    x = {}
    for val in params.type_letters.split(","):
        if "hira_std" == val:
            x.update(hiragana.hira_std)
        if "hira_tenmaru" == val:
            x.update(hiragana.hira_tenmaru)
        if "hira_yoon" == val:
            x.update(hiragana.hira_yoon)
        if "kata_std" == val:
            x.update(katakana.kata_std)
        if "kata_tenmaru" == val:
            x.update(katakana.kata_tenmaru)
        if "kata_yoon" == val:
            x.update(katakana.kata_yoon)
    lettersKey, lettersVal = generate_lettersgana(x)
    return lettersVal


@router.post("/")
async def check_letters(user_input: CheckLetters) -> dict[str, Any]:
    global \
        lettersKey, \
        lettersVal, \
        score_hira, \
        score_kata, \
        score_hira_wrong, \
        score_kata_wrong
    msg = None
    if user_input.key_input == lettersKey:
        for val in hiragana.hiraganas.values():
            if lettersVal == val:
                score_hira += 1
                break
        for val in katakana.katakanas.values():
            if lettersVal == val:
                score_kata += 1
                break
    else:
        msg = f"The correct answer is: {lettersKey}"
        for val in hiragana.hiraganas.values():
            if lettersVal == val:
                score_hira_wrong += 1
                break
        for val in katakana.katakanas.values():
            if lettersVal == val:
                score_kata_wrong += 1
                break

    result = {
        "message": msg,
        "score_hira_correct": score_hira,
        "score_kata_correct": score_kata,
        "score_hira_wrong": score_hira_wrong,
        "score_kata_wrong": score_kata_wrong,
    }
    return result
