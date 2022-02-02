from fastapi import FastAPI
from database import engine

app = FastAPI()


@app.get("/")
def index():
    return {"message": "OK", "engine": engine.table_names}