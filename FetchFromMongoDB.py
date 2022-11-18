import pymongo
import pandas as pd
client = pymongo.MongoClient("mongodb+srv://yashvij:0000@cluster0.wnq7l.mongodb.net/?retryWrites=true&w=majority")
db = client.test
db1 = client["MultipleMongoData"]
collectionsMultiple = db1['CollectionMultipleData']
## Retriving data From Mongo DB

data_find = collectionsMultiple.find({
    'age':{"$gt":20}

})


df1 = pd.DataFrame(data_find)
df1.to_excel("MongoData.xlsx")
