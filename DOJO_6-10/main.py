from fastapi import FastAPI, Response, Request, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from pydantic import BaseModel
import uvicorn
from sessiondb import Sessions
import db_utils as db
load_dotenv()  # Load environment variables

# Create the FastAPI instance
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
sessionManager = Sessions(db.db_config, secret_key=db.session_config['session_key'], expiry=600)

"""
Create user and visitor classes that match our SQL schema
"""
class User(BaseModel):
    username: str
    password: str
    email: str
    first_name: str
    last_name: str

class Visitor(BaseModel):
    username: str
    password: str

"""
Helper function to see if a user is authenticated
"""
def is_authenticated(username:str, password:str) -> bool:
    return db.check_user_password(username, password)

@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("wordle.html", {"request": request, 'users': db.select_users()})

@app.get('/users')
def get_users() -> dict:
    users = db.select_users()
    keys = ['id', 'first_name', 'last_name', 'username', 'email']
    users = [dict(zip(keys, user)) for user in users]
    return {"users": users}

@app.get('/users/{user_id}')
def get_user(user_id: int) -> dict:
    user = db.select_users(user_id)
    if user:
        return {'id': user[0], 'username': user[1], 'email': user[2], 'first_name': user[3], 'last_name': user[4]}
    return {}

@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: User, response: Response):
    new_id = db.create_user(user.username, user.password, user.email, user.first_name, user.last_name)
    print(new_id)
    if new_id == 0:
        response.status_code = status.HTTP_418_IM_A_TEAPOT
        return
    return get_user(new_id)


@app.get("/wordle", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def get_wordle(request: Request):
    # would be nice if we had a function to check if someone is logged in
    session = sessionManager.get_session(request)
    if len(session) > 0 and session.get('logged_in'):
        return templates.TemplateResponse("wordle.html", {"request": request})
    else:
        return RedirectResponse("/", status_code=302)



@app.get("/logout", response_class=HTMLResponse)
async def get_logout(request: Request):
    secret_hash = request.headers.get("Authorization")
    if not secret_hash:
        return RedirectResponse("/", status_code=302)
    auth.user_logout(secret_hash)
    return RedirectResponse("/", status_code=302)

@app.post('/login', status_code=status.HTTP_200_OK)
def post_login(visitor: Visitor, request: Request, response: Response) -> dict:
    username = visitor.username
    password = visitor.password

    # Invalidate previous session if logged in
    session = sessionManager.get_session(request)
    if len(session) > 0:
        sessionManager.end_session(request, response)

    # Authenticate the user
    if db.check_user_password(username, password):
        session_data = {'username': username, 'logged_in': True}
        session_id = sessionManager.create_session(response, session_data)
        return {'message': 'Login successful', 'session_id': session_id}
    else:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {'message': 'Invalid username or password', 'session_id': 0}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

