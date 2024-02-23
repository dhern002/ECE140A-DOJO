import db_utils
def authenticate_user(username:str, password:str) -> bool:
    if db_utils.check_user_password(username, password):
        return True

    return False

def is_user_logged_in(secret_hash):
    # check if hash exist in sessions table
    # and if it has expired or not

def user_logout(secret_hash):
    # should delete the has from the sessions table