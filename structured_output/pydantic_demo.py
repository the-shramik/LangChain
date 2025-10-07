from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = "shramik"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5.0, description="representing the cgpa of the student")


new_student = {"age":24, "email":"abc@gmail.com", "cgpa":4.0}

student = Student(**new_student)

#  converting object to dictionary
student_dict = dict(student)

print(student_dict['age'])

#  converting object to json
student_json = student.model_dump_json()

print(student_json)