import numpy as np
from plots import Plotter


vertices = 20
map_size = vertices * 10

x = np.random.randint(map_size, size=vertices)
y = np.random.randint(map_size, size=vertices)
coordinates = (x, y)

MDVRP_map = Plotter(coordinates=coordinates)
MDVRP_map.plot_all()
# MDVRP_map.plot_edges()
# MDVRP_map.show_map()
