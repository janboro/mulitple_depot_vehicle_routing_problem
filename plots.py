import matplotlib.pyplot as plt


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
            s=120,
            zorder=2,
        )

    def plot_vertices(self):
        x = [depo.x for depo in self.problem_map.vertices]
        y = [depo.y for depo in self.problem_map.vertices]
        plt.scatter(
            x,
            y,
            color="blue",
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

    def plot_all(self):
        self.plot_depots()
        self.plot_vertices()
        self.plot_edges()
        self.show_map()

    def show_map(self):
        plt.show()
