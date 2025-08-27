from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class Data:
    n1:int
    n2:int 
    result:int
    
class MyData(BaseModel):
     num1: int
     num2: int
     answer: int