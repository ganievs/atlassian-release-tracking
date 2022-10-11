from fastapi import FastAPI, HTTPException
from pydantic import BaseSettings
from app.model import Url
from app.controller import parse_url, check_version, version_compare
import os 


class Settings(BaseSettings):
    database_url: str = "/tmp/data.db"

settings = Settings()
app = FastAPI()

@app.get("/", status_code=200)
def dummy():
    return {"status": "ok"}

@app.post("/", status_code=201)
def proceed_url(payload: Url):
    data = parse_url(payload.url)
    name = payload.product
    version = version_compare(data)
    resp = check_version(name, version, settings.database_url)
    return resp
