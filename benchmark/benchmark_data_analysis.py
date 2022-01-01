import json
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def get_z_cost(data, column, x_axis, y_axis):
    z = []
    for _, row in data.iterrows():
        if row[column] is not np.NaN:
            str_row = row[column].replace("'", '"')
            final_row = json.loads(str_row)
            cost = final_row["total_distance"]
            z.append(cost)

    i = 0
    new_z = []
    while len(z) > 0:
        cost = 0.0
        for _ in range(3):
            cost += z.pop(0)
        cost /= 3
        new_z.append(cost)
    Z = []

    for _ in y_axis:
        z_row = []
        for _ in x_axis:
            z_row.append(new_z.pop(0))
        Z.append(z_row)
    Z = np.array(Z)
    return Z


def get_z_axis(data, column, x_axis, y_axis):
    z = []

    for element in data:
        z.append(element[1][column].mean(axis=0))
    Z = []
    for _ in y_axis:
        z_row = []
        for _ in x_axis:
            z_row.append(z.pop(0))
        Z.append(z_row)
    Z = np.array(Z)
    return Z


def plot_3d(X, Y, Z, title, z_label, x_label="Number of depots", y_label="Number of vertices"):
    plt.figure()
    ax = plt.axes(projection="3d")
    ax.plot_wireframe(X, Y, Z)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_zlabel(z_label)
    return plt


def main():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    csv_file_path = os.path.normpath(os.path.join(current_directory, "benchmark_data/MDVRP_benchmark.csv"))
    benchmark_data = pd.read_csv(csv_file_path)
    grouped_benchmark_data = pd.read_csv(csv_file_path).groupby(["no_of_depots", "no_of_vertices"])

    x_axis = np.arange(50, 1001, 50)
    y_axis = np.arange(1, 21)
    X, Y = np.meshgrid(x_axis, y_axis)
    min_max_y_axis = np.arange(2, 21)
    min_max_X, min_max_Y = np.meshgrid(x_axis, min_max_y_axis)

    # Execution times
    Z_NN = get_z_axis(
        data=grouped_benchmark_data, column="nearest_neighbour_execution_time", x_axis=x_axis, y_axis=y_axis
    )
    Z_NN_min_max = get_z_axis(
        data=grouped_benchmark_data, column="nearest_neighour_min_max_execution_time", x_axis=x_axis, y_axis=y_axis
    )
    Z_NI = get_z_axis(
        data=grouped_benchmark_data, column="nearest_insertion_execution_time", x_axis=x_axis, y_axis=y_axis
    )
    Z_NI_min_max = get_z_axis(
        data=grouped_benchmark_data, column="nearest_insertion_min_max_execution_time", x_axis=x_axis, y_axis=y_axis
    )

    NN_plot = plot_3d(X=X, Y=Y, Z=Z_NN, z_label="Execution_time", title="Nearest Neighbour")
    NN_min_max_plot = plot_3d(X=X, Y=Y, Z=Z_NN_min_max, z_label="Execution_time", title="Nearest Neighbour Min Max")
    NI_plot = plot_3d(X=X, Y=Y, Z=Z_NI, z_label="Execution_time", title="Nearest Insertion")
    NI_min_max_plot = plot_3d(X=X, Y=Y, Z=Z_NI_min_max, z_label="Execution_time", title="Nearest Insertion Min Max")
    plt.show()

    # Costs
    Z_NN_cost = get_z_cost(data=benchmark_data, column="nearest_neighbour_distances", x_axis=x_axis, y_axis=y_axis)
    Z_NN_min_max_cost = get_z_cost(
        data=benchmark_data, column="nearest_neighour_min_max_distances", x_axis=x_axis, y_axis=min_max_y_axis
    )
    Z_NI_cost = get_z_cost(data=benchmark_data, column="nearest_insertion_distances", x_axis=x_axis, y_axis=y_axis)
    Z_NI_min_max_cost = get_z_cost(
        data=benchmark_data, column="nearest_insertion_min_max_distances", x_axis=x_axis, y_axis=min_max_y_axis
    )

    Z_NN_plot = plot_3d(X=X, Y=Y, Z=Z_NN_cost, z_label="Total cost", title="Nearest Neighbour")
    Z_NN_min_max_plot = plot_3d(
        X=min_max_X, Y=min_max_Y, Z=Z_NN_min_max_cost, z_label="Total cost", title="Nearest Neighbour min max"
    )
    Z_NI_plot = plot_3d(X=X, Y=Y, Z=Z_NI_cost, z_label="Total cost", title="Nearest Insertion")
    Z_NI_min_max_plot = plot_3d(
        X=min_max_X, Y=min_max_Y, Z=Z_NI_min_max_cost, z_label="Total cost", title="Nearest Insertion min max"
    )
    plt.show()


if __name__ == "__main__":
    main()
