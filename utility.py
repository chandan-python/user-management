import pymongo

connection_string = 'mongodb://localhost:27017/'
client = pymongo.MongoClient(connection_string)

db = client['instagram_data'] 

mycollection = db['followers_data']  
credentilas_collection = db['followers_data']
