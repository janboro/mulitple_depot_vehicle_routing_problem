import matplotlib.pyplot as plt
import numpy as np


class Plotter:
    def __init__(self, VRP, no_of_depots, title="MDVRP"):
        self.VRP = VRP
        self.title = title
        self.no_of_depots = no_of_depots
        self.colors = self.generate_colors(no_of_depots=no_of_depots)

    def generate_colors(self, no_of_depots):
        colors = []
        for _ in range(no_of_depots):
            colors.append(tuple(np.random.randint(256, size=3) / 256))
        return colors

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
            if depot.path != []:
                for i in range(len(depot.path) - 1):
                    x1 = depot.path[i].x
                    x2 = depot.path[i + 1].x
                    y1 = depot.path[i].y
                    y2 = depot.path[i + 1].y
                    plt.plot(
                        [x1, x2],
                        [y1, y2],
                        color="C3",
                        zorder=1,
                        lw=2,
                    )

    def plot_group(self):
        for depot in self.VRP.depots:
            color = self.colors[depot.index]
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
