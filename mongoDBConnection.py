import pymongo

client = pymongo.MongoClient("mongodb+srv://yashvij:0000@cluster0.wnq7l.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

data = {
    "name":"Yash",
    "ID":101,
    "Address" : "Delhi"
}
db1 = client['Mongotest11']
collection1 = db1['coll1']
collection1.insert_one(data)


