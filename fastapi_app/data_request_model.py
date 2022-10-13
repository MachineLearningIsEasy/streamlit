from pydantic import BaseModel, validator, root_validator
from typing import Optional


class MlRequest(BaseModel):
    carat: float
    cut: str
    color: str
    clarity: str
    depth: float
    table: float
    x: float
    y: float
    z: float