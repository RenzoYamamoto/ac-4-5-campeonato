from functools import wraps
from flask import redirect, session


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        
        return f(*args, **kwargs)
    return decorated_function
