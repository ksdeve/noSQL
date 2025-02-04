# db_connection.py
from pymongo import MongoClient

def get_db_connection():
    # Connexion à MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client.mydb
    collection = db.mycollection
    return collection
