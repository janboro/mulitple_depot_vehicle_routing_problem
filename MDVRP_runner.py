import pprint
from utils import get_execution_time
from MDVRP import MDVRP


def main():
    pp = pprint.PrettyPrinter(indent=4)
    # Generating
    mdvrp = MDVRP(no_of_vertices=500, no_of_depots=10, map_size=1000)

    # Nearest Neighbour
    mdvrp.solver.assign_vertices_to_depot()
    mdvrp.solver.solve_nearest_neighbour()

    # Plotting
    mdvrp.plotter.plot_initial_map()
    mdvrp.plotter.show_map()

    mdvrp.plotter.plot_group()
    mdvrp.plotter.show_map()

    mdvrp.plotter.plot_group()
    mdvrp.plotter.plot_path()
    mdvrp.plotter.show_map(title="Nearest Neighbour")

    # Reseting
    mdvrp.solver.reset_solution()

    # Nearest insertion
    mdvrp.solver.solve_nearest_insertion()

    mdvrp.plotter.plot_group()
    mdvrp.plotter.plot_path()
    mdvrp.plotter.show_map(title="Nearest Insertion")


if __name__ == "__main__":
    main()
