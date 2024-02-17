from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import mysql.connector
from dotenv import load_dotenv
import os
import uvicorn
import asyncio

load_dotenv()  # Load environment variables

# Create the FastAPI instance
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


def get_db_connection():
    return mysql.connector.connect(
        host="db", # because we are inside docker compose, we can use the service name as the host name
        user="root",
        password=os.getenv('MYSQL_ROOT_PASSWORD'),
        database=os.getenv('MYSQL_DATABASE')
    )

@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("wordle.html", {"request": request})

@app.post("/create-user")
async def create_user(request: Request):
    json = await request.json()
    username = json["username"]
    password = json["password"]
    print(json)
    return json
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

