from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name : str = 'Ravi'
    Age: Optional[int]= None
    email : EmailStr
    Marks : float = Field(gt=0, lt=10, default= 5.0)


new_student = {'name': 'Ravi Dubey'}
new_student = {'Age': 44}
new_student = {'Age': '32','email' : 'ravi@gmail.com'}

student = Student(**new_student)
print(student)