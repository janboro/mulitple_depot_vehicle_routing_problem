import pprint
from utils import get_execution_time
from MDVRP import MDVRP


def main():
    pp = pprint.PrettyPrinter(indent=4)
    # Generating
    mdvrp = MDVRP(no_of_vertices=50, no_of_depots=3, map_size=1000)

    # Nearest Neighbour

    assigning_time = get_execution_time(function=mdvrp.solver.assign_vertices_to_depot)
    print(f"Assigning time: {assigning_time}")

    NN_time = get_execution_time(function=mdvrp.solver.solve_nearest_insertion)
    print(f"Nearest Neighbour execution time: {NN_time}")
    # distances = mdvrp.get_distances()
    # # print(f"Distances: \n{distances}")
    # print(f"Distances:")
    # pp.pprint(distances)

    # print()
    # NN_min_max_time = get_execution_time(
    #     function=mdvrp.solver.run_min_max, TSP_function=mdvrp.solver.solve_nearest_neighbour
    # )
    # print(f"Nearest Neighbour min max execution time: {NN_min_max_time}")

    # mdvrp.solver.run_min_max(TSP_function=mdvrp.solver.solve_nearest_neighbour)
    # # Plotting
    mdvrp.plotter.plot_initial_map()
    mdvrp.plotter.show_map()

    mdvrp.plotter.plot_group()
    mdvrp.plotter.show_map()

    mdvrp.plotter.plot_group()
    mdvrp.plotter.plot_path()
    mdvrp.plotter.show_map()

    # # Reseting
    # mdvrp.solver.reset_solution()

    # # Nearest insertion
    # NI_start_time = time.time()
    # mdvrp.solver.solve_nearest_insertion()
    # NI_end_time = time.time()
    # NI_total_distance = 0
    # for depot in mdvrp.VRP.depots:
    #     NI_total_distance += depot.route_cost
    #     print(f"Index: {depot.index}, cost: {depot.route_cost}")
    # print(f"Total NI distance: {round(NI_total_distance)}")
    # print(f"Nearest Insertion execution time: {round(NI_end_time - NI_start_time, 6)}")

    # mdvrp.plotter.plot_group()
    # mdvrp.plotter.plot_path()
    # mdvrp.plotter.show_map()


if __name__ == "__main__":
    main()
