from pydantic import BaseModel, Field
from fastapi import Query


class CheckLetters(BaseModel):
    key_input: str


class LettersAll(BaseModel):
    type_letters: str = Field(
        Query(
            None,
            description="If you want 2 or more values, just type it and seperate by comma (,) | List of type: hira_std, hira_tenmaru, hira_yoon, kata_std, kata_tenmaru, kata_yoon",
        )
    )
