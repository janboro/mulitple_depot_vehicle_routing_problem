import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, coordinates, title="MDVRP"):
        self.coordinates = coordinates
        plt.figure()
        plt.axis("off")
        plt.title(title)

    def plot_vertices(self):
        plt.scatter(self.coordinates[0], self.coordinates[1], s=60, zorder=2)

    def plot_edges(self):
        plt.plot(self.coordinates[0], self.coordinates[1], color="C3", zorder=1, lw=2)

    def plot_all(self):
        self.plot_vertices()
        self.plot_edges()
        self.show_map()

    def show_map(self):
        plt.show()
