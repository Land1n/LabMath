from enum import Enum

from dataclasses import dataclass


class TypeClassicalButton(Enum):
    NORMAL = 0
    ERROR = 1

@dataclass
class DataSample:
    symbol:str
    name:str
    device_error:str
    values:list[int]