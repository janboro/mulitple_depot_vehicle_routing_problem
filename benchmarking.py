import csv
import os
from utils import get_execution_time
from MDVRP import MDVRP


def main():
    for no_of_depots in range(1, 21):
        for no_of_vertices in range(50, 1001, 50):
            for _ in range(3):
                # print(f"no_of_depots: {no_of_depots}\nearest_neighouro_of_vertices: {no_of_vertices}")
                data_row = [no_of_depots, no_of_vertices]
                # Generating map
                mdvrp = MDVRP(no_of_vertices=no_of_vertices, no_of_depots=no_of_depots, map_size=1000)

                # Assigning vertices to depots
                assigning_time = get_execution_time(function=mdvrp.solver.assign_vertices_to_depot)
                data_row.append(assigning_time)
                # print(f"assigning_time: {assigning_time}")

                # Nearest Neighbour
                nearest_neighbour_execution_time = get_execution_time(function=mdvrp.solver.solve_nearest_neighbour)
                nearest_neighbour_distances = mdvrp.get_distances()
                data_row.append(nearest_neighbour_execution_time)
                data_row.append(nearest_neighbour_distances)
                # print(f"nearest_neighbour_execution_time: {nearest_neighbour_execution_time}")
                # print(f"nearest_neighbour_distances: {nearest_neighbour_distances}")

                # Nearest Neighbour min max
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
                # print(f"nearest_neighour_min_max_time: {nearest_neighour_min_max_time}")
                # print(f"nearest_neighour_min_max_distances: {nearest_neighour_min_max_distances}")
                mdvrp.solver.reset_solution()
                # Nearest Insertion
                nearest_insertion_execution_time = get_execution_time(function=mdvrp.solver.solve_nearest_insertion)
                nearest_insertion_distances = mdvrp.get_distances()
                data_row.append(nearest_insertion_execution_time)
                data_row.append(nearest_insertion_distances)
                # print(f"nearest_insertion_execution_time: {nearest_insertion_execution_time}")
                # print(f"nearest_insertion_distances: {nearest_insertion_distances}")

                # Nearest Insertion min max
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
                # print(f"nearest_insertion_min_maxexecution__time: {nearest_insertion_min_max_texecution_ime}")
                # print(f"nearest_insertion_min_max_distances: {nearest_insertion_min_max_distances}")
                print("Finished loop\n")

                current_directory = os.path.dirname(os.path.realpath(__file__))
                csv_file_path = os.path.normpath(os.path.join(current_directory, "MDVRP_benchmark.csv"))
                with open(csv_file_path, "a") as f:
                    write = csv.writer(f)
                    write.writerow(data_row)


if __name__ == "__main__":
    main()
