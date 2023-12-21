import csv
import os

from MDVRP import MDVRP


def run_road_distribution_benchmark():
    # Generating
    no_of_depots: int = 10
    no_of_vertices: int = 1000
    mdvrp: MDVRP = MDVRP(no_of_vertices=no_of_vertices, no_of_depots=no_of_depots, map_size=1000)

    # Nearest Insertion
    mdvrp.solver.assign_vertices_to_depot()
    mdvrp.solver.solve_nearest_insertion()

    distances: dict[str, float] = mdvrp.get_distances()
    print(f"Initial distance:\n{distances}")
    data_row: list[str | dict[str, float]] = ["nearest_insertion", distances]

    current_directory: str = os.path.dirname(os.path.realpath(__file__))
    csv_file_path: str = os.path.normpath(os.path.join(current_directory, "benchmark_data/road_distributions2.csv"))
    with open(csv_file_path, "a") as f:
        write = csv.writer(f)
        write.writerow(data_row)

    # Plotting Initial solution
    mdvrp.plotter.plot_group()
    mdvrp.plotter.plot_path()
    mdvrp.plotter.show_map()

    # Min Max optimization
    for i in range(50):
        mdvrp.solver.run_min_max(TSP_function=mdvrp.solver.solve_nearest_insertion)
        min_max_distances: dict[str, float] = mdvrp.get_distances()
        data_row = [f"nearest_insertion_min_max_{i}", min_max_distances]

        with open(csv_file_path, "a") as f:
            write = csv.writer(f)
            write.writerow(data_row)
        print(f"{i} distances:\n{mdvrp.get_distances()}")

    mdvrp.plotter.plot_group()
    mdvrp.plotter.plot_path()
    mdvrp.plotter.show_map()


if __name__ == "__main__":
    run_road_distribution_benchmark()
