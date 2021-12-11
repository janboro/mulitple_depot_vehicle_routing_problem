import numpy as np
from data_types.coordinates import Coordinates


class MapGenerator:
    def __init__(self, vertices_number, depots_number):
        self.depots_number = depots_number
        self.vertices_number = vertices_number
        self.map_size = (vertices_number + depots_number) * 10
        self.depots = []
        self.vertices = []

    def generate_depots(self):
        index = range(self.depots_number)
        x = np.random.randint(self.map_size, size=self.depots_number)
        y = np.random.randint(self.map_size, size=self.depots_number)
        for i in range(len(index)):
            depo = Coordinates(
                index=index[i],
                x=x[i],
                y=y[i],
            )
            self.depots.append(depo)

    def generate_vertices(self):
        index = range(self.vertices_number)
        x = np.random.randint(self.map_size, size=self.vertices_number)
        y = np.random.randint(self.map_size, size=self.vertices_number)
        for i in range(len(index)):
            vertice = Coordinates(
                index=index[i],
                x=x[i],
                y=y[i],
            )
            self.vertices.append(vertice)

    def generate_map(self):
        self.generate_depots()
        self.generate_vertices()
