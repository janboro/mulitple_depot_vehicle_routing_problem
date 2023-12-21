import csv
import os

from MDVRP import MDVRP
from utils.timer import get_execution_time


def run_algorithm_benchmarking():
    no_of_depots: int
    no_of_vertices: int
    for no_of_depots in range(1, 21):
        for no_of_vertices in range(50, 1001, 50):
            for _ in range(3):
                print(f"no_of_depots: {no_of_depots}\nno_of_vertices: {no_of_vertices}")
                data_row: list[int | float | dict[str, float] | None] = [no_of_depots, no_of_vertices]
                # Generating problem
                mdvrp: MDVRP = MDVRP(no_of_vertices=no_of_vertices, no_of_depots=no_of_depots, map_size=1000)

                # Assigning vertices to depots
                assigning_time: float = get_execution_time(function=mdvrp.solver.assign_vertices_to_depot)
                data_row.append(assigning_time)

                # Nearest Neighbour
                nearest_neighbour_execution_time: float = get_execution_time(
                    function=mdvrp.solver.solve_nearest_neighbour
                )
                nearest_neighbour_distances: dict[str, float] = mdvrp.get_distances()
                data_row.append(nearest_neighbour_execution_time)
                data_row.append(nearest_neighbour_distances)

                # Nearest Neighbour min max
                nearest_neighour_min_max_execution_time: float | None
                nearest_neighour_min_max_distances: dict[str, float] | None
                if no_of_depots > 1:
                    nearest_neighour_min_max_execution_time = get_execution_time(
                        function=mdvrp.solver.run_min_max, TSP_function=mdvrp.solver.solve_nearest_neighbour
                    )
                    nearest_neighour_min_max_distances = mdvrp.get_distances()
                else:
                    nearest_neighour_min_max_execution_time = None
                    nearest_neighour_min_max_distances = None
                data_row.append(nearest_neighour_min_max_execution_time)
                data_row.append(nearest_neighour_min_max_distances)

                mdvrp.solver.reset_solution()

                # Nearest Insertion
                nearest_insertion_execution_time: float = get_execution_time(
                    function=mdvrp.solver.solve_nearest_insertion
                )
                nearest_insertion_distances: dict[str, float] = mdvrp.get_distances()
                data_row.append(nearest_insertion_execution_time)
                data_row.append(nearest_insertion_distances)

                # Nearest Insertion min max
                nearest_insertion_min_max_execution_time: float | None
                nearest_insertion_min_max_distances: dict[str, float] | None
                if no_of_depots > 1:
                    nearest_insertion_min_max_execution_time = get_execution_time(
                        function=mdvrp.solver.run_min_max, TSP_function=mdvrp.solver.solve_nearest_insertion
                    )
                    nearest_insertion_min_max_distances = mdvrp.get_distances()
                else:
                    nearest_insertion_min_max_execution_time = None
                    nearest_insertion_min_max_distances = None
                data_row.append(nearest_insertion_min_max_execution_time)
                data_row.append(nearest_insertion_min_max_distances)

                current_directory: str = os.path.dirname(os.path.realpath(__file__))
                csv_file_path: str = os.path.normpath(
                    os.path.join(current_directory, "benchmark_data/MDVRP_benchmark.csv")
                )
                with open(csv_file_path, "a") as f:
                    write = csv.writer(f)
                    write.writerow(data_row)


if __name__ == "__main__":
    run_algorithm_benchmarking()
