# pylint: disable=too-few-public-methods
from pydantic import BaseModel


class Vertice(BaseModel):
    index: int
    x: int
    y: int
    visited: bool = False


class Depot(BaseModel):
    index: int
    x: int
    y: int
    assigned_vertices: list = []
    path: list[Vertice] = []
    route_cost: float = 0.0
