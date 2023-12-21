import numpy as np

from data_types.coordinates import Depot, Vertice


class Map:
    def __init__(self, no_of_vertices: int, no_of_depots: int, map_size: int) -> None:
        self.no_of_depots: int = no_of_depots
        self.no_of_vertices: int = no_of_vertices
        self.map_size: int = map_size
        self.depots: list[Depot] = []
        self.vertices: list[Vertice] = []
        self.generate_map()

    def generate_depots(self) -> None:
        x: np.ndarray = np.random.randint(self.map_size, size=self.no_of_depots)
        y: np.ndarray = np.random.randint(self.map_size, size=self.no_of_depots)
        for i in range(self.no_of_depots):
            depot: Depot = Depot(index=i, x=x[i], y=y[i])
            self.depots.append(depot)

    def generate_vertices(self) -> None:
        x: np.ndarray = np.random.randint(self.map_size, size=self.no_of_vertices)
        y: np.ndarray = np.random.randint(self.map_size, size=self.no_of_vertices)
        for i in range(self.no_of_vertices):
            vertice: Vertice = Vertice(index=i, x=x[i], y=y[i])
            self.vertices.append(vertice)

    def generate_map(self) -> None:
        self.generate_depots()
        self.generate_vertices()
