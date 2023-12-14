from MDVRP import MDVRP


def main() -> None:
    # Generating map for the problem
    mdvrp: MDVRP = MDVRP(no_of_vertices=500, no_of_depots=10, map_size=1000)

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
