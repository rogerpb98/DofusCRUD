import pymongo
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db=client["Dofus"]
collection = db["Almanax"]

result = collection.find( { "categories": { "$in": ["Combat Xp"] } } ).limit(5)
data = []
for x in result:
    data.append(x)
    #pprint(x)

pprint(data)
# Issue the serverStatus command and print the results
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)