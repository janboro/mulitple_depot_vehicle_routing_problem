from map_generator import MapGenerator
from plots import Plotter
from solver import MDVRPSolver


class MDVRP:
    def __init__(self, no_of_vertices, no_of_depots):
        self.VRP = MapGenerator(no_of_vertices=no_of_vertices, no_of_depots=no_of_depots)
        self.solver = MDVRPSolver(VRP=self.VRP)
        self.plotter = Plotter(VRP=self.VRP)


def main():
    mdvrp = MDVRP(no_of_vertices=20, no_of_depots=3)
    mdvrp.VRP.generate_map()

    mdvrp.solver.assign_vertices_to_depot()

    mdvrp.solver.solve_NN()

    mdvrp.plotter.plot_initial_map()
    mdvrp.plotter.show_map()

    mdvrp.plotter.plot_group()
    mdvrp.plotter.show_map()

    mdvrp.plotter.plot_group()
    mdvrp.plotter.plot_path()
    mdvrp.plotter.show_map()


if __name__ == "__main__":
    main()
