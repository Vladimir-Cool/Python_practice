from flask import session
from functools import wraps

def Chek_Logged(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if 'logged_in' in session:
            return func(*args,**kwargs)
        return 'Вы НЕ в системе'
    return wrapper
