from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class Data:
    n1:int
    n2:int 
    result:int
    
