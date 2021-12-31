import numpy as np
from data_types.coordinates import Depot, Vertice


class MapGenerator:
    def __init__(self, no_of_vertices, no_of_depots, map_size):
        self.no_of_depots = no_of_depots
        self.no_of_vertices = no_of_vertices
        self.map_size = map_size
        self.depots = []
        self.vertices = []
        self.generate_map()

    def generate_depots(self):
        index = range(self.no_of_depots)
        x = np.random.randint(self.map_size, size=self.no_of_depots)
        y = np.random.randint(self.map_size, size=self.no_of_depots)
        for i in range(len(index)):
            depot = Depot(index=index[i], x=x[i], y=y[i])
            self.depots.append(depot)

    def generate_vertices(self):
        index = range(self.no_of_vertices)
        x = np.random.randint(self.map_size, size=self.no_of_vertices)
        y = np.random.randint(self.map_size, size=self.no_of_vertices)
        for i in range(len(index)):
            vertice = Vertice(
                index=index[i],
                x=x[i],
                y=y[i],
            )
            self.vertices.append(vertice)

    def generate_map(self):
        self.generate_depots()
        self.generate_vertices()
