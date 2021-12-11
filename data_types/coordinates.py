# pylint: disable=too-few-public-methods
from pydantic import BaseModel


class Coordinates(BaseModel):
    index: int
    x: int
    y: int
    assigned_depo: int = None
