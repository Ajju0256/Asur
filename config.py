import os
from pymongo import MongoClient


# Flask configuration
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')


client = MongoClient('localhost', 27017)
DATABASE = client["asur"]




