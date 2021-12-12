import matplotlib.pyplot as plt
import numpy as np


class Plotter:
    def __init__(self, VRP, title="MDVRP"):
        self.VRP = VRP
        self.title = title
        self.initialize_map(title=title)

    def initialize_map(self, title):
        plt.figure()

    def plot_depots(self):
        x = [depot.x for depot in self.VRP.depots]
        y = [depot.y for depot in self.VRP.depots]
        plt.scatter(
            x,
            y,
            color="black",
            s=140,
            zorder=2,
        )
        plt.scatter(
            x,
            y,
            color="steelblue",
            s=100,
            zorder=3,
        )

    def plot_vertices(self):
        x = [vertice.x for vertice in self.VRP.vertices]
        y = [vertice.y for vertice in self.VRP.vertices]
        plt.scatter(
            x,
            y,
            color="steelblue",
            s=60,
            zorder=2,
        )

    def plot_path(self):
        for depot in self.VRP.depots:
            # Connecting depot to beggining of path
            plt.plot(
                [depot.x, depot.path[0].x],
                [depot.y, depot.path[0].y],
                color="C3",
                zorder=1,
                lw=2,
            )
            # Connecting end of path to depo
            plt.plot(
                [depot.x, depot.path[-1].x],
                [depot.y, depot.path[-1].y],
                color="C3",
                zorder=1,
                lw=2,
            )

            for i in range(1, len(depot.path)):
                x1 = depot.path[i - 1].x
                x2 = depot.path[i].x
                y1 = depot.path[i - 1].y
                y2 = depot.path[i].y
                plt.plot(
                    [x1, x2],
                    [y1, y2],
                    color="C3",
                    zorder=1,
                    lw=2,
                )

    def plot_group(self):
        for depot in self.VRP.depots:
            color = tuple(np.random.randint(256, size=3) / 256)
            plt.scatter(
                depot.x,
                depot.y,
                color="black",
                s=140,
                zorder=2,
            )
            plt.scatter(
                depot.x,
                depot.y,
                color=[color],
                s=100,
                zorder=3,
            )
            for vertice in depot.assigned_vertices:
                plt.scatter(
                    vertice.x,
                    vertice.y,
                    color=[color],
                    s=60,
                    zorder=3,
                )

    def plot_initial_map(self):
        self.plot_depots()
        self.plot_vertices()

    def show_map(self):
        plt.title(self.title)
        plt.axis("off")
        plt.show()
