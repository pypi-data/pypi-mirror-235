from pydantic import BaseModel
from typing import Any

class WebsocketMessage(BaseModel):
    Type: str
    Data: Any