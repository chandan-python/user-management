from dotenv import dotenv_values
from pymongo import MongoClient
# Load the variables from the .env file
env_vars = dotenv_values('.env')

MONGO_USER_NAME = env_vars['MONGO_USER_NAME']
MONGO_PASSWORD = env_vars['MONGO_PASSWORD']
MONGO_HOST = env_vars['MONGO_HOST']
MONGO_PORT = env_vars['MONGO_PORT']


connection_string = f"mongodb://{MONGO_USER_NAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/mydatabase?authSource=admin"
# connection_string = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/"

client = MongoClient(connection_string)

db = client.mydatabase
user_collection = db.users 
print(connection_string)

# user_collection.insert_one({'name':'chandan'})
