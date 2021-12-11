import matplotlib.pyplot as plt
import numpy as np


class Plotter:
    def __init__(self, problem_map, title="MDVRP"):
        self.problem_map = problem_map
        self.initialize_map(title=title)

    def initialize_map(self, title):
        plt.figure()
        plt.axis("off")
        plt.title(title)

    def plot_depots(self):
        x = [depo.x for depo in self.problem_map.depots]
        y = [depo.y for depo in self.problem_map.depots]
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
        x = [depo.x for depo in self.problem_map.vertices]
        y = [depo.y for depo in self.problem_map.vertices]
        plt.scatter(
            x,
            y,
            color="steelblue",
            s=60,
            zorder=2,
        )

    def plot_edges(self):
        x = [depo.x for depo in self.problem_map.vertices]
        y = [depo.y for depo in self.problem_map.vertices]
        plt.plot(
            x,
            y,
            color="C3",
            zorder=1,
            lw=2,
        )

    def plot_group(self):
        for depo in self.problem_map.depots:
            color = tuple(np.random.randint(256, size=3) / 256)
            plt.scatter(
                depo.x,
                depo.y,
                color="black",
                s=140,
                zorder=2,
            )
            plt.scatter(
                depo.x,
                depo.y,
                color=[color],
                s=100,
                zorder=3,
            )
            for vertice in self.problem_map.vertices:
                if vertice.assigned_depo == depo.index:
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
        plt.show()
