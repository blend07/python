from typing import Optional
from typing import Any
from typing import Union
from typing import List

def process_anything(value: Any)->str:
    return f"Processed {value}"

print(process_anything(1))

def process_value(value: Union[int,str]) -> str:
    if isinstance(value, int):
        return f"Number: {value}"
    return f"String: {value}"

print(process_value("Digital School"))


def sum_list(value: List[int])->int:
    return sum(numbers)

numbers: List[int] = [1,2,3]
result: int = sum_list(numbers)