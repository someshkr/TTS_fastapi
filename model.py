from pydantic import BaseModel
from typing import Optional, final

class InputData(BaseModel):
    data: str

