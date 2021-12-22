#!/usr/bin/python
# coding=utf-8

from datetime import datetime
from model import Almanax
# MongoDB async driver
import motor.motor_asyncio

conn = motor.motor_asyncio.AsyncIOMotorClient("mongodb://127.0.0.1:27017/")
database = conn.Dofus
collection = database.Almanax

async def fetch_all_almanax():
    today_date = datetime.today().strftime("%Y-%m-%d")
    list = []
    cursor = collection.find({ "date": { "$gte": today_date } })
    async for x in cursor:
        list.append(Almanax(**x))
    return list

async def fetch_today():
    today_date = datetime.today().strftime("%Y-%m-%d")
    list = []
    cursor = collection.find({ "date": { "$eq": today_date } })
    async for x in cursor:
        list.append(Almanax(**x))
    return list

async def fetch_tomorrow():
    today_date = datetime.today().strftime("%Y-%m-%d")
    list = []
    cursor = collection.find({ "date": { "$gt": today_date } }).limit(1)
    async for x in cursor:
        list.append(Almanax(**x))
    return list

async def fetch_week():
    today_date = datetime.today().strftime("%Y-%m-%d")
    list = []
    cursor = collection.find({ "date": { "$gt": today_date } }).limit(7)
    async for x in cursor:
        list.append(Almanax(**x))
    return list

async def fetch_next_almanax_variable(limit):
    today_date = datetime.today().strftime("%Y-%m-%d")
    list = []
    cursor = collection.find({ "date": { "$gt": today_date } }).limit(limit)
    async for x in cursor:
        list.append(Almanax(**x))
    return list

async def fetch_all_from_category(category):
    today_date = datetime.today().strftime("%Y-%m-%d")
    list = []
    cursor = collection.find( { "$and": [ { "date": { "$gt": today_date } }, { "categories": {"$in": [category] } }] } )
    async for x in cursor:
        list.append(Almanax(**x))
    return list

async def fetch_next_from_category(category):
    today_date = datetime.today().strftime("%Y-%m-%d")
    list = []
    cursor = collection.find( { "$and": [ { "date": { "$gt": today_date } }, { "categories": {"$in": [category] } }] } ).limit(1)
    async for x in cursor:
        list.append(Almanax(**x))
    return list

async def fetch_ten_from_category(category):
    today_date = datetime.today().strftime("%Y-%m-%d")
    list = []
    cursor = collection.find( { "$and": [ { "date": { "$gt": today_date } }, { "categories": {"$in": [category] } }] } ).limit(10)
    async for x in cursor:
        list.append(Almanax(**x))
    return list

async def fetch_multiple_from_category(category, limit):
    today_date = datetime.today().strftime("%Y-%m-%d")
    list = []
    cursor = collection.find( { "$and": [ { "date": { "$gt": today_date } }, { "categories": {"$in": [category] } }] } ).limit(limit)
    async for x in cursor:
        list.append(Almanax(**x))
    return list