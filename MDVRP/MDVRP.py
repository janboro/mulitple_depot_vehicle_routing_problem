from data_types.coordinates import Depot
from MDVRP.map_generator import Map
from MDVRP.plotter import MDVRPPlotter
from MDVRP.solver import MDVRPSolver


class MDVRP:
    def __init__(self, no_of_vertices: int, no_of_depots: int, map_size: int) -> None:
        self.VRP: Map = Map(no_of_vertices=no_of_vertices, no_of_depots=no_of_depots, map_size=map_size)
        self.solver: MDVRPSolver = MDVRPSolver(VRP=self.VRP)
        self.plotter: MDVRPPlotter = MDVRPPlotter(VRP=self.VRP, no_of_depots=no_of_depots)

    def get_distances(self) -> dict[str, float]:
        distances: dict[str, float] = {}
        total_distance: float = 0.0

        depot: Depot
        for depot in self.VRP.depots:
            total_distance += depot.route_cost
            distances[f"depot_{depot.index}"] = depot.route_cost
        distances["total_distance"] = total_distance
        return distances
