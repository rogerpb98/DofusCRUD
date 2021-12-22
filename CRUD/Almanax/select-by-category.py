from CRUD import connectToMongo

collection = connectToMongo
result = collection.find( { "categories": { "$in": ["Combat Xp"] } } ).limit(5)
data = []
for x in result:
    data.append(x)
    #pprint(x)

#pprint(data)