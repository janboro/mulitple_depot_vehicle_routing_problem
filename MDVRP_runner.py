from map_generator import MapGenerator
from plots import Plotter
from solver import MDVRPSolver

my_map = MapGenerator(vertices_number=20, depots_number=3)
my_map.generate_map()

solver = MDVRPSolver(problem_map=my_map)
solver.assign_vertices_to_depo()

map_plot = Plotter(problem_map=my_map)
map_plot.plot_all()
