from pydantic import BaseModel


class CheckHiragana(BaseModel):
    key_input: str
