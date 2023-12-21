from MDVRP.MDVRP import MDVRP
from config.config_handler import get_MDVRP_params


def main() -> None:
    # Loading parameters
    params: dict[str, int] = get_MDVRP_params()
    # Generating map for the problem
    mdvrp: MDVRP = MDVRP(
        no_of_vertices=params["no_of_vertices"], no_of_depots=params["no_of_depots"], map_size=params["map_size"]
    )

    # Solving the routing problem with the Nearest Neighbour algorithm
    mdvrp.solver.assign_vertices_to_depot()
    mdvrp.solver.solve_nearest_neighbour()

    # Plotting initial map to find routes
    mdvrp.plotter.plot_initial_map()
    mdvrp.plotter.show_map()

    # Plotting the map with divided districts for route planning
    mdvrp.plotter.plot_group()
    mdvrp.plotter.show_map()

    # Plotting the Nearest Neighbour algorithm routes
    mdvrp.plotter.plot_group()
    mdvrp.plotter.plot_path()
    mdvrp.plotter.show_map(title="Nearest Neighbour")

    # Reseting
    mdvrp.solver.reset_solution()

    mdvrp.solver.solve_nearest_insertion()

    # Plotting the Nearest Insertion algorithm routes
    mdvrp.plotter.plot_group()
    mdvrp.plotter.plot_path()
    mdvrp.plotter.show_map(title="Nearest Insertion")


if __name__ == "__main__":
    main()
