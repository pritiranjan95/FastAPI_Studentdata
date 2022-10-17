from distutils.config import PyPIRCCommand
from http import client
from lib2to3.pgen2.token import COLONEQUAL
import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client["Student"]
collection=db["stu_data"]

