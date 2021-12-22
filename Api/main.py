from fastapi import FastAPI, Path, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

from db import (
    fetch_one_almanax,
    fetch_all_almanax,
)
@app.get("/")
async def home():
    return {"Data": "Test"}

# Will return a list of commands Almanax related
@app.get("/Almanax/")
async def almanax():
    #return almanaxesEntity(conn.find())
    #result = conn.find()
    #data = []
    #for x in result:
    #    data.append(x)
    #return data
    return {"Data": "Almanax"}

# Will return a list of all bonuses from the database
@app.get("/Almanax/All")
async def get_all_almanax():
    response = await fetch_all_almanax()
    return response

# Will return today's almanax
@app.get("/Almanax/Today")
def almanax():
    data = fetch_one_almanax()
    return {"Data": "Almanax"}

# Will return tomorrow's almanax
@app.get("/Almanax/Tomorrow")
async def almanax():
    date = "2022-01-01"
    response = fetch_one_almanax(date)
    if response:
        return response
    raise HTTPException(404, "No data found")

# Will return next week's almanax
@app.get("/Almanax/Week")
async def almanax():
    return {"Data": "Almanax"}

# Will return the next "x" days of almanax
@app.get("/Almanax/{limit}")
async def almanax(
    limit: int = Path(None, description = "The number of days you want to get")
    ):
    return {"Data": "Almanax"}

# Will return a list with every day that fall into said category
@app.get("/Almanax/Category/{category}")
async def get_almanax_by_category(
    category: str = Path(None, description = "The name of the Category you want to filter by")
    ):
    return {"Data": category}

# Will return a list with the next 10 days that fall into said category
@app.get("/Almanax/Category/{category}/Ten")
async def get_almanax_by_category(
    category: str = Path(None, description = "The name of the Category you want to filter by")
    ):
    return {"Data": category}

# Will return a list with a set number of days that fall into said category
@app.get("/Almanax/Category/{category}/{limit}")
async def get_almanax_by_category_limit(
    category: str = Path(None, description = "The name of the Category you want to filter by"), 
    limit: int = Path(None, description = "The number of results you want to get from this query")
    ):
    return {"Data": "/Almanax/Category/limit"}