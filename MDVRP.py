from map_generator import MapGenerator
from plots import Plotter
from solver import MDVRPSolver


class MDVRP:
    def __init__(self, no_of_vertices, no_of_depots, map_size):
        self.VRP = MapGenerator(no_of_vertices=no_of_vertices, no_of_depots=no_of_depots, map_size=map_size)
        self.solver = MDVRPSolver(VRP=self.VRP)
        self.plotter = Plotter(VRP=self.VRP, no_of_depots=no_of_depots)

    def get_distances(self):
        distances = {}
        total_distance = 0
        for depot in self.VRP.depots:
            total_distance += depot.route_cost
            distances[f"depot_{depot.index}"] = depot.route_cost
        distances["total_distance"] = total_distance
        return distances
