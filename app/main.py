from fastapi import FastAPI, HTTPException
from app.model import Url
from app.controller import get_product, parse_url, check_version, version_compare
import os 


DATABASE_URL = os.getenv("DATABASE_URL", default="/data/data.db")

app = FastAPI()

@app.post("/", status_code=201)
def proceed_url(payload: Url):
    data = parse_url(payload.url)
    name = get_product(payload.url)
    version = version_compare(data)
    resp = check_version(name, version, DATABASE_URL)
    return resp
