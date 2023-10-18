import jsonpickle
import json
from dataclasses import dataclass

@dataclass
class File():

    path:str
    fileName:str
    fileType:str
    mtime:int

    def __str__(self) -> str:
        return jsonpickle.encode(self)
    def __repr__(self) -> str:
        return self.__str__()
    def to_json(obj):
        return json.dumps(obj, default=lambda obj: obj.__dict__)
