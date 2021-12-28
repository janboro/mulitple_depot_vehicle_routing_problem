import time
from map_generator import MapGenerator
from plots import Plotter
from solver import MDVRPSolver


class MDVRP:
    def __init__(self, no_of_vertices, no_of_depots, map_size):
        self.VRP = MapGenerator(no_of_vertices=no_of_vertices, no_of_depots=no_of_depots, map_size=map_size)
        self.solver = MDVRPSolver(VRP=self.VRP)
        self.plotter = Plotter(VRP=self.VRP)


def main():
    # Generating
    mdvrp = MDVRP(no_of_vertices=200, no_of_depots=8, map_size=1000)
    mdvrp.VRP.generate_map()

    # Nearest Neighbour
    mdvrp.solver.assign_vertices_to_depot()

    NN_start_time = time.time()
    mdvrp.solver.solve_nearest_neighbour()
    NN_end_time = time.time()
    NN_total_distance = 0
    for depot in mdvrp.VRP.depots:
        NN_total_distance += depot.route_cost
        print(f"Index: {depot.index}, cost: {depot.route_cost}")
    print(f"Total NN distance: {round(NN_total_distance)}")
    print(f"Nearest Neighbour execution time: {round(NN_end_time - NN_start_time, 6)}")
    print()

    # Plotting
    mdvrp.plotter.plot_initial_map()
    mdvrp.plotter.show_map()

    mdvrp.plotter.plot_group()
    mdvrp.plotter.show_map()

    mdvrp.plotter.plot_group()
    mdvrp.plotter.plot_path()
    mdvrp.plotter.show_map()

    # Reseting
    mdvrp.solver.reset_solution()

    # Nearest insertion
    NI_start_time = time.time()
    mdvrp.solver.solve_nearest_insertion()
    NI_end_time = time.time()
    NI_total_distance = 0
    for depot in mdvrp.VRP.depots:
        NI_total_distance += depot.route_cost
        print(f"Index: {depot.index}, cost: {depot.route_cost}")
    print(f"Total NI distance: {round(NI_total_distance)}")
    print(f"Nearest Insertion execution time: {round(NI_end_time - NI_start_time, 6)}")

    mdvrp.plotter.plot_group()
    mdvrp.plotter.plot_path()
    mdvrp.plotter.show_map()


if __name__ == "__main__":
    main()
