#!/usr/bin/python
# coding=utf-8

from fastapi import FastAPI, Path, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

from db import (
    fetch_all_almanax,
    fetch_today,
    fetch_tomorrow,
    fetch_week,
    fetch_next_almanax_variable,
    fetch_all_from_category,
    fetch_next_from_category,
    fetch_ten_from_category,
    fetch_multiple_from_category,
)
@app.get("/")
async def home():
    return {"Data": "Test"}

# Will return a list of commands Almanax related
@app.get("/Almanax/")
async def almanax():
    return {"Data": "Almanax"}

# Returns a list of all bonuses from the database
@app.get("/Almanax/All")
async def get_all_almanax():
    response = await fetch_all_almanax()
    return response

# Returns today's almanax
@app.get("/Almanax/Today")
async def get_today():
    response = await fetch_today()
    if response:
        return response
    raise HTTPException(404, "No data found")

# Returns tomorrow's almanax
@app.get("/Almanax/Tomorrow")
async def get_tomorrow():
    response = await fetch_tomorrow()
    if response:
        return response
    raise HTTPException(404, "No data found")

# Returns next week's almanax
@app.get("/Almanax/Week")
async def get_week():
    response = await fetch_week()
    if response:
        return response
    raise HTTPException(404, "No data found")

# Returns the next "x" days of almanax
@app.get("/Almanax/Next/{limit}")
async def get_next_almanax_variable(
    limit: int = Path(None, description = "The number of days you want to get")
    ):
    response = await fetch_next_almanax_variable(limit)
    if response:
        return response
    raise HTTPException(404, "No data found")

# Will return a list with every day that fall into said category
@app.get("/Almanax/Category/{category}")
async def get_all_from_category(
    category: str = Path(None, description = "The name of the Category you want to filter by")
    ):
    response = await fetch_all_from_category(category)
    if response:
        return response
    raise HTTPException(404, "No data found")

# Will return a list with the next 10 days that fall into said category
@app.get("/Almanax/Category/{category}/Next")
async def get_next_from_category(
    category: str = Path(None, description = "The name of the Category you want to filter by")
    ):
    response = await fetch_next_from_category(category)
    if response:
        return response
    raise HTTPException(404, "No data found")

# Will return a list with the next 10 days that fall into said category
@app.get("/Almanax/Category/{category}/Ten")
async def get_ten_from_category(
    category: str = Path(None, description = "The name of the Category you want to filter by")
    ):
    response = await fetch_ten_from_category(category)
    if response:
        return response
    raise HTTPException(404, "No data found")

# Will return a list with a set number of days that fall into said category
@app.get("/Almanax/Category/{category}/{limit}")
async def get_almanax_by_category_limit(
    category: str = Path(None, description = "The name of the Category you want to filter by"), 
    limit: int = Path(None, description = "The number of results you want to get from this query")
    ):
    response = await fetch_multiple_from_category(category, limit)
    if response:
        return response
    raise HTTPException(404, "No data found")