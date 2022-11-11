from fastapi import FastAPI
from bson.json_util import dumps
from models.students import Student   #importing the model here
from service.operations import create_student, delete_data,show_student, update_student
from utils.mongo import collection

app=FastAPI()

# @app.post("/create")
# def data_in(student:Student):
#    a=student.dict()
#    collection.insert_one(a)

@app.get("/")
def show():
    return "HI THERE"

@app.post("/create")
def data_in(student:Student):
   create_student(student)


# @app.get("/show/{name}")
# def display(name:str):
#     a={"name":name}
#     data = dumps(collection.find(a))
    #     return data

@app.get("/find/{name}")
def search(name:str):
    a=show_student(name)
    return a


# @app.put("/update/student/{name}")
# def change(name:str,student:Student):
#     a= student.dict()
#     # stu = collection.find_one({"name":name})
#     # print()
#     collection.update_one({"name":name},{"$set":a}  )
#     return "Updated Successfully"

#Editing the existing data

@app.put("/{name}")
def change_student(name:str, student:Student):
    update_student(name,student)
    

#delete api
@app.delete("/delte/student/{name}")
def delete(name):
    status = delete_data(name)
    return status