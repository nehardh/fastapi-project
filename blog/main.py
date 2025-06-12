from fastapi import FastAPI
from typing import Optional
from . import schemas

app = FastAPI()

@app.post("/blog")
def create_blog(request: schemas.Blog):
    return request