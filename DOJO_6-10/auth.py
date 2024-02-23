from functools import wraps
from fastapi.requests import Request
from fastapi.responses import RedirectResponse, Response
from sessiondb import Sessions
import db_utils as db


sessionManager = Sessions(db.db_config, secret_key=db.session_config['session_key'], expiry=600)


def login(username: str, password: str, request: Request, response: Response) -> bool:
    """
    Function to check if the user is in the database and the password is correct
    If the a session already exists, the user is logged in
    :param username:
    :param password:
    :param request:
    :param response:
    :return:
    """
    session = sessionManager.get_session(request)
    if len(session) > 0:
        logout(request, response)

    if db.check_user_password(username, password):
        sessionManager.create_session(response, {'username': username, 'logged_in': True})
        return True
    return False


def logout(request: Request, response: Response) -> bool:
    """
    Function to log out the user
    :param request:
    :param response:
    :return:
    """
    secret_hash = request.headers.get("Authorization")
    if not secret_hash:
        return False
    session = sessionManager.get_session(request)
    if len(session) > 0:
        sessionManager.end_session(request, response)
        return True
    return False


def logged_in(func):
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):

        session = sessionManager.get_session(request)

        if len(session) > 0:
            return func(request, *args, **kwargs)  # Pass the request
        else:
            return RedirectResponse("/", status_code=302)

    return wrapper
