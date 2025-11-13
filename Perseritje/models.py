from pydantic import BaseModel, FieldValidationInfo, field_validator, constr, conint
from typing import Optional, Any, Union

class user(BaseModel):
    id: int
    name:str
    age: Optional[int] = None
    email: Optional[str] = None

    @field_validator('age')
    def age_must_be_positive(cls, v, info:FieldValidationInfo):
        if v<=0:
            raise ValueError('Age must be positive')
        return v
    
#example

try:
    user1 = user(id=1, name="John Doe", age=2)
except ValueError as e:
    print(e)


class address(BaseModel):
    street: str
    city: str
    
class another_user(BaseModel):
    id: conint(gt=0)
    name: constr(min_length=2, max_length=50)

def get_name(name:Optional[str]= None) -> str:
    if name:
        return name
    return "Anonymous"

print(get_name())

def process_value(value: Union[int,str]) -> str:
    if isinstance(value,int):
        return f"Number: {value}"
    return f"String: {value}"

print(process_value())

def process_anything(value:Any) ->str:
    return f"Processed {value}"

print(process_anything())