# 1. import fastAPI from FastAPI class
from fastapi import FastAPI

# 2. create app object of fastAPI application
app = FastAPI()

# 3. define endpoint
@app.get("/")   # home url route
# 4. create method/function for this endpoint
def hello():
    return {'msg':'Python Backend'}

# create other endpoints
@app.get("/about")
def about():
    return {'msg':'Welcome to our second fastapi endpoint'}

