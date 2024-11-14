from fastapi import FastAPI
from routes import routers

app: FastAPI = FastAPI(title="Wakana Quizz")

app.include_router(routers)


@app.get("/")
async def hello() -> dict[str, str]:
    return {"Hello": "World"}
