import pandas as pd
import pymongo
df = pd.read_csv("bank/bank.csv",sep=";")
print(df.head())
df.reset_index(inplace=True)
mongoData = df.to_dict("records")
client = pymongo.MongoClient("mongodb+srv://yashvij:0000@cluster0.wnq7l.mongodb.net/?retryWrites=true&w=majority")
db = client.test
db1 = client["MultipleMongoData"]
collectionsMultiple = db1['CollectionMultipleData']
collectionsMultiple.insert_many(mongoData)