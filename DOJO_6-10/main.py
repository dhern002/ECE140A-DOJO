from fastapi import FastAPI, Response, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import uvicorn
import db_utils as db
from auth import logged_in, logout, login
from models import User, Visitor

# Load environment variables
load_dotenv()

# Create the FastAPI instance
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


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
@logged_in  # Decorator to check if user is logged in
async def get_wordle(request: Request):
    return templates.TemplateResponse("wordle.html", {"request": request})


@app.get("/logout", response_class=HTMLResponse)
async def get_logout(request: Request, response: Response):
    logout(request, response)
    return RedirectResponse("/", status_code=302)


@app.post('/login', status_code=status.HTTP_200_OK)
def post_login(visitor: Visitor, request: Request, response: Response, next_route="/") -> RedirectResponse:
    username = visitor.username
    password = visitor.password

    # Authenticate the user
    if login(username, password, request, response):
        # why do we have to set cookie here?
        return RedirectResponse(next_route, status_code=200, headers={'set-cookie': response.headers.get("set-cookie")})
    else:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return RedirectResponse("/", status_code=401)


@app.get('/protected')
@logged_in
def get_protected() -> dict:
    return {'message': 'Access granted'}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
