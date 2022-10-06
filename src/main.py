import uvicorn
from fastapi import fastapi
import os
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

@app.post("/", response_model=Url)
def proceed_url(url: Url):
    return 

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
