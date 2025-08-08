# patient management system --->
from fastapi import FastAPI
import json

app = FastAPI()

# create an helper function -- to load data from patients.json file
def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {'msg':'Patient Management System API'}

@app.get("/about")
def about():
    return {'msg':'A fully functional API to manage your patient records'}

# endpoint which will give all the patients data to our client
@app.get("/view")
def view():
    # fetch that data
    data = load_data()
    return data

