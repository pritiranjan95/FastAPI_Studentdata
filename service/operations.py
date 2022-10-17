from utils.mongo import collection
from models.students import Student
from bson.json_util import dumps

def create_student(student):
    a=student.dict()     
    return collection.insert_one(a)

def show_student(name):
    a={"name":name}
    return dumps(collection.find(a))

def update_student(key,student):
    a={"name":key}
    b={"$set":student.dict()}
    return collection.update_one(a,b)

def delete_data(key):
    a={"name":key}
    collection.delete_one(a)
    return "suss"

