from tkinter.messagebox import NO
from pydantic import BaseModel

class Student(BaseModel):
    name:str  | None=None
    age:int | None=None
    section:str | None=None
