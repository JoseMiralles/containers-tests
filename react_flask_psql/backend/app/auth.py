from flask import request
from functools import wraps

def authorize(func):
    @wraps(func)
    def inner(required_role):
        print(request)
    return inner
