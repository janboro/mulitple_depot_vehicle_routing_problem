import json
import os
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.core.groupby import DataFrameGroupBy


def compare_results(results1: np.ndarray, results2: np.ndarray) -> float:
    if np.shape(results1) == (19, 20):
        empty_array: np.ndarray = np.empty((1, 20))
        empty_array[:] = np.NaN
        results1 = np.concatenate((empty_array, results1), axis=0)

    if np.shape(results2) == (19, 20):
        empty_array: np.ndarray = np.empty((1, 20))
        empty_array[:] = np.NaN
        results2 = np.concatenate((empty_array, results2), axis=0)

    result: np.ndarray = np.divide(results1, results2)
    row_mean: list[float] = []
    for row in result:
        if True in np.isnan(row):
            pass
        else:
            row_mean.append(np.mean(row))
    return float(np.mean(row_mean))


def get_z_cost(data: pd.DataFrame, column: str, x_axis: np.ndarray, y_axis: np.ndarray) -> np.ndarray:
    z: list[float] = []
    row: pd.Series
    for _, row in data.iterrows():
        if row[column] is not np.NaN:
            str_row: str = str(row[column]).replace("'", '"')
            final_row: dict[Any, Any] = json.loads(str_row)
            cost: float = final_row["total_distance"]
            z.append(cost)

    new_z: list[float] = []
    while len(z) > 0:
        cost: float = 0.0
        for _ in range(3):
            cost += z.pop(0)
        cost /= 3
        new_z.append(cost)
    Z: list[list[float]] = []

    for _ in y_axis:
        z_row: list[float] = []
        for _ in x_axis:
            z_row.append(new_z.pop(0))
        Z.append(z_row)
    return np.array(Z)


def get_z_cost_for_2d(data: pd.DataFrame, column: str, x_axis: np.ndarray, y_axis: np.ndarray) -> np.ndarray:
    z: list[float] = []
    row: pd.Series
    for _, row in data.iterrows():
        if row["no_of_depots"] == 10:
            if row["no_of_vertices"] == 500:
                if row[column] is not np.NaN:
                    str_row: str = str(row[column]).replace("'", '"')
                    final_row: dict[Any, Any] = json.loads(str_row)
                    cost: float = final_row["total_distance"]
                    z.append(cost)

    new_z: list[float] = []
    while len(z) > 0:
        cost: float = 0.0
        for _ in range(3):
            cost += z.pop(0)
        cost /= 3
        new_z.append(cost)

    Z: list[list[float]] = []
    for _ in y_axis:
        z_row: list[float] = []
        for _ in x_axis:
            z_row.append(new_z.pop(0))
        Z.append(z_row)
    return np.array(Z)


def get_z_axis(data: pd.DataFrame, column: str, x_axis: np.ndarray, y_axis: np.ndarray):
    z: list[float] = []

    for element in data:
        z.append(element[1][column].mean(axis=0))
    Z: list[list[float]] = []
    for _ in y_axis:
        z_row: list[float] = []
        for _ in x_axis:
            z_row.append(z.pop(0))
        Z.append(z_row)
    return np.array(Z)


def plot_3d(X, Y, Z, title, z_label, x_label="Number of depots", y_label="Number of vertices"):
    plt.figure()
    ax = plt.axes(projection="3d")
    ax.plot_wireframe(X, Y, Z)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_zlabel(z_label)
    return plt


def plotting_2d(data, x_axis, y_axis):
    cost = get_z_cost_for_2d(data=data, column="nearest_neighbour_distances", x_axis=x_axis, y_axis=y_axis)
    print(cost)


# def compare_execution_times():
#     # Setup
#     Z_NN = get_z_axis(
#         data=grouped_benchmark_data, column="nearest_neighbour_execution_time", x_axis=x_axis, y_axis=y_axis
#     )
#     # Z_NN_min_max = get_z_axis(
#     #     data=grouped_benchmark_data, column="nearest_neighour_min_max_execution_time", x_axis=x_axis, y_axis=y_axis
#     # )
#     # Z_NI = get_z_axis(
#     #     data=grouped_benchmark_data, column="nearest_insertion_execution_time", x_axis=x_axis, y_axis=y_axis
#     # )
#     # Z_NI_min_max = get_z_axis(
#     #     data=grouped_benchmark_data, column="nearest_insertion_min_max_execution_time", x_axis=x_axis, y_axis=y_axis
#     # )
#     # Comparision
#     time_comparision = []
#     for i in [Z_NN, Z_NN_min_max, Z_NI, Z_NI_min_max]:
#         time_row_comparision = []
#         for j in [Z_NN, Z_NN_min_max, Z_NI, Z_NI_min_max]:
#             comp = compare_results(results1=i, results2=j)
#             time_row_comparision.append(comp)
#         time_comparision.append(time_row_comparision)
#     names = ["Nearest Neighbour", "Nearest Neighbour Min-Max", "Nearest Insertion", "Nearest Insertion Min-Max"]
#     df = pd.DataFrame.from_records(time_comparision)
#     df.columns = names
#     print(df)
#     fig, ax = plt.subplots()
#     im = ax.imshow(time_comparision, cmap="Blues")
#     # im = ax.imshow(time_comparision)

#     ax.set_xticks(np.arange(len(names)))
#     ax.set_yticks(np.arange(len(names)))
#     ax.set_xticklabels(names)
#     ax.set_yticklabels(names)

#     plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

#     print(tabulate(time_comparision, headers=names))
#     # for i in range(len(names)):
#     #     for j in range(len(names)):
#     #         text = ax.text(j, i, round(time_comparision[i][j], 4), ha="center", va="center", color="black")

#     # ax.set_title(f"Avg execution time comparison")
#     # fig.tight_layout()
#     # cbar = fig.colorbar(im)
#     # cbar.ax.set_xlabel("Performance")
#     # plt.show()


def analyze_nearest_neighbour(grouped_benchmark_data: DataFrameGroupBy):
    # Execution times
    # Calculations
    # Z_assigning = get_z_axis(data=grouped_benchmark_data, column="assigning_time", x_axis=x_axis, y_axis=y_axis)
    Z_NN = get_z_axis(
        data=grouped_benchmark_data, column="nearest_neighbour_execution_time", x_axis=x_axis, y_axis=y_axis
    )

    #

    # comp = compare_results(results1=Z_NN, results2=Z_NN_min_max)

    # Plots
    NN_plot = plot_3d(X=X, Y=Y, Z=Z_NN, z_label="Execution_time", title="Nearest Neighbour")
    NN_plot.show()

    Z_NN_cost = get_z_cost(data=benchmark_data, column="nearest_neighbour_distances", x_axis=x_axis, y_axis=y_axis)
    # Plots
    Z_NN_plot = plot_3d(X=X, Y=Y, Z=Z_NN_cost, z_label="Total cost", title="Nearest Neighbour")
    # Z_NN_min_max_plot = plot_3d(
    #     X=min_max_X, Y=min_max_Y, Z=Z_NN_min_max_cost, z_label="Total cost", title="Nearest Neighbour min max"
    # )
    # Z_NI_plot = plot_3d(X=X, Y=Y, Z=Z_NI_cost, z_label="Total cost", title="Nearest Insertion")
    # Z_NI_min_max_plot = plot_3d(
    #     X=min_max_X, Y=min_max_Y, Z=Z_NI_min_max_cost, z_label="Total cost", title="Nearest Insertion min max"
    # )
    Z_NN_plot.show()


def analyze_nearest_neighbour_min_max():
    pass


def analyze_nearest_insertion():
    pass


def analyze_nearest_insertion_min_max():
    pass


def main():
    current_directory: str = os.path.dirname(os.path.realpath(__file__))
    csv_file_path: str = os.path.normpath(os.path.join(current_directory, "benchmark_data/MDVRP_benchmark.csv"))
    benchmark_data: pd.DataFrame = pd.read_csv(csv_file_path)
    grouped_benchmark_data: DataFrameGroupBy = pd.read_csv(csv_file_path).groupby(["no_of_depots", "no_of_vertices"])

    x_axis: np.ndarray = np.arange(50, 1001, 50)
    y_axis: np.ndarray = np.arange(1, 21)
    X, Y = np.meshgrid(x_axis, y_axis)
    min_max_y_axis = np.arange(2, 21)
    min_max_X, min_max_Y = np.meshgrid(x_axis, min_max_y_axis)

    plotting_2d(benchmark_data, x_axis, y_axis)

    # Execution times
    # Calculations
    # Z_assigning = get_z_axis(data=grouped_benchmark_data, column="assigning_time", x_axis=x_axis, y_axis=y_axis)
    Z_NN = get_z_axis(
        data=grouped_benchmark_data, column="nearest_neighbour_execution_time", x_axis=x_axis, y_axis=y_axis
    )
    # Z_NN_min_max = get_z_axis(
    #     data=grouped_benchmark_data, column="nearest_neighour_min_max_execution_time", x_axis=x_axis, y_axis=y_axis
    # )
    # Z_NI = get_z_axis(
    #     data=grouped_benchmark_data, column="nearest_insertion_execution_time", x_axis=x_axis, y_axis=y_axis
    # )
    # Z_NI_min_max = get_z_axis(
    #     data=grouped_benchmark_data, column="nearest_insertion_min_max_execution_time", x_axis=x_axis, y_axis=y_axis
    # )

    # # Comparision
    # time_comparision = []
    # for i in [Z_NN, Z_NN_min_max, Z_NI, Z_NI_min_max]:
    #     time_row_comparision = []
    #     for j in [Z_NN, Z_NN_min_max, Z_NI, Z_NI_min_max]:
    #         comp = compare_results(results1=i, results2=j)
    #         time_row_comparision.append(comp)
    #     time_comparision.append(time_row_comparision)
    # names = ["Nearest Neighbour", "Nearest Neighbour Min-Max", "Nearest Insertion", "Nearest Insertion Min-Max"]
    # df = pd.DataFrame.from_records(time_comparision)
    # df.columns = names
    # print(df)
    # fig, ax = plt.subplots()
    # im = ax.imshow(time_comparision, cmap="Blues")
    # # im = ax.imshow(time_comparision)

    # ax.set_xticks(np.arange(len(names)))
    # ax.set_yticks(np.arange(len(names)))
    # ax.set_xticklabels(names)
    # ax.set_yticklabels(names)

    # plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # print(tabulate(time_comparision, headers=names))

    # for i in range(len(names)):
    #     for j in range(len(names)):
    #         text = ax.text(j, i, round(time_comparision[i][j], 4), ha="center", va="center", color="black")

    # ax.set_title(f"Avg execution time comparison")
    # fig.tight_layout()
    # cbar = fig.colorbar(im)
    # cbar.ax.set_xlabel("Performance")
    # plt.show()

    # comp = compare_results(results1=Z_NN, results2=Z_NN_min_max)

    # # Plots
    # assigning_plot = plot_3d(X=X, Y=Y, Z=Z_assigning, z_label="Execution_time", title="Assigning vertices to depots")
    # NN_plot = plot_3d(X=X, Y=Y, Z=Z_NN, z_label="Execution_time", title="Nearest Neighbour")
    # NN_min_max_plot = plot_3d(X=X, Y=Y, Z=Z_NN_min_max, z_label="Execution_time", title="Nearest Neighbour Min Max")
    # NI_plot = plot_3d(X=X, Y=Y, Z=Z_NI, z_label="Execution_time", title="Nearest Insertion")
    # NI_min_max_plot = plot_3d(X=X, Y=Y, Z=Z_NI_min_max, z_label="Execution_time", title="Nearest Insertion Min Max")
    # plt.show()

    # Costs
    # Calculations
    Z_NN_cost = get_z_cost(data=benchmark_data, column="nearest_neighbour_distances", x_axis=x_axis, y_axis=y_axis)
    # Z_NN_min_max_cost = get_z_cost(
    #     data=benchmark_data, column="nearest_neighour_min_max_distances", x_axis=x_axis, y_axis=min_max_y_axis
    # )
    # Z_NI_cost = get_z_cost(data=benchmark_data, column="nearest_insertion_distances", x_axis=x_axis, y_axis=y_axis)
    # Z_NI_min_max_cost = get_z_cost(
    #     data=benchmark_data, column="nearest_insertion_min_max_distances", x_axis=x_axis, y_axis=min_max_y_axis
    # )
    # # Comparison
    # cost_comparision = []
    # for i in [Z_NN_cost, Z_NN_min_max_cost, Z_NI_cost, Z_NI_min_max_cost]:
    #     cost_row_comparision = []
    #     for j in [Z_NN_cost, Z_NN_min_max_cost, Z_NI_cost, Z_NI_min_max_cost]:
    #         comp = compare_results(results1=i, results2=j)
    #         cost_row_comparision.append(comp)
    #     cost_comparision.append(cost_row_comparision)
    # names = ["Nearest Neighbour", "Nearest Neighbour Min-Max", "Nearest Insertion", "Nearest Insertion Min-Max"]
    # df = pd.DataFrame.from_records(cost_comparision)
    # df.columns = names
    # print(df)

    # fig, ax = plt.subplots()
    # im = ax.imshow(cost_comparision, cmap="Blues")
    # # im = ax.imshow(cost_comparision)

    # ax.set_xticks(np.arange(len(names)))
    # ax.set_yticks(np.arange(len(names)))
    # ax.set_xticklabels(names)
    # ax.set_yticklabels(names)

    # plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # print(tabulate(cost_comparision, headers=names))

    # for i in range(len(names)):
    #     for j in range(len(names)):
    #         text = ax.text(j, i, round(cost_comparision[i][j], 4), ha="center", va="center", color="black")

    # ax.set_title(f"Avg total cost comparison")
    # fig.tight_layout()
    # cbar = fig.colorbar(im)
    # cbar.ax.set_xlabel("Performance")
    # plt.show()

    # Plots
    Z_NN_plot = plot_3d(X=X, Y=Y, Z=Z_NN_cost, z_label="Total cost", title="Nearest Neighbour")
    # Z_NN_min_max_plot = plot_3d(
    #     X=min_max_X, Y=min_max_Y, Z=Z_NN_min_max_cost, z_label="Total cost", title="Nearest Neighbour min max"
    # )
    # Z_NI_plot = plot_3d(X=X, Y=Y, Z=Z_NI_cost, z_label="Total cost", title="Nearest Insertion")
    # Z_NI_min_max_plot = plot_3d(
    #     X=min_max_X, Y=min_max_Y, Z=Z_NI_min_max_cost, z_label="Total cost", title="Nearest Insertion min max"
    # )
    plt.show()


if __name__ == "__main__":
    main()
