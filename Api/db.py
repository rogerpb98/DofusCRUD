from model import Almanax
# MongoDB async driver
import motor.motor_asyncio

conn = motor.motor_asyncio.AsyncIOMotorClient("mongodb://127.0.0.1:27017/")
database = conn.Dofus
collection = database.Almanax

async def fetch_one_almanax(date):
    document = await collection.find_one()
    return document

async def fetch_all_almanax():
    list = []
    cursor = collection.find()
    async for x in cursor:
        list.append(Almanax(**x))
    return list

async def create_almanax(almanax):
    document = almanax
    result = await collection.insert_one(document)
    return document

async def remove_almanax(date):
    await collection.delete_one( { "date": date } )
    return True
#conn = MongoClient("mongodb://127.0.0.1:27017/")["Dofus"]["Almanax"]