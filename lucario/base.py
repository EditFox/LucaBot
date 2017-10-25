import json
functions = {}

def lucafunc(func):
    functions[func.__name__] = func
    return func
    
    
with open('config.json') as data:
    config = json.load(data)
