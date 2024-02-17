from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import mysql.connector
from dotenv import load_dotenv
import os
import uvicorn
import asyncio
# import auth

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


@app.get("/wordle", response_class=HTMLResponse)
async def get_wordle(request: Request):
    # would be nice if we had a function to check if someone is logged in
    secret_hash = ""
    if auth.is_user_logged_in(secret_hash):
        return templates.TemplateResponse("wordle.html", {"request": request})
    else:
        return RedirectResponse("/login")


@app.get("/logout", response_class=HTMLResponse)
async def get_logout(request: Request):
    secret_hash = request.headers.get("Authorization")
    if not secret_hash:
        return RedirectResponse("/", status_code=302)
    auth.user_logout(secret_hash)
    return RedirectResponse("/", status_code=302)

@app.post("/login")
async def log_in(request: Request):
    print(request.headers.get("Authorization"))
    print(request.headers.get("User-Agent"))
    return {"login" : True}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

