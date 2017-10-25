import json
functions = {}
docstrings = {}

def lucafunc(func):
    functions[func.__name__] = func
    docstrings[func.__name__] = func.__doc__
    return func
    
    
with open('config.json') as data:
    config = json.load(data)
