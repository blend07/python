from pydantic import BaseModel , conint , constr
from typing import Optional

# class User(BaseModel):
#     id: int
#     name: str
#     age: int
#     email: str
    
    
# user=User(id=1, name="Lis", age=20, email="lis@gmail.com")
# print(user)

class User(BaseModel):
    id: int
    name:str
    age: Optional[int]=15
    email: Optional[str]="example@gmail.com"

user1=User(id=1, name="Lis", age=20, email="lis@gmail.com")
print(user1)
user2=User(id=2, name="Darsej", email="darsej@gmail.com")
print(user2)
user3=User(id=3, name="Darsej")
print(user3)


class User2(BaseModel):
    id: conint(gt=0)
    name: constr(min_length=2, max_length=50)

valid_user = User2(id=1,name="Lis")
print(valid_user)
# valid_user1 = User2(id=0,name="Darsej")
# print(valid_user1) gabim