from pydoc import cli
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient(port=27017)
db = client["python-mid-project"]
books_collection = db["books"]
books = books_collection.find({})
# for book in books:
#     print(book)
