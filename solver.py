import numpy as np
from data_types.coordinates import Depot, Vertice


class MDVRPSolver:
    def __init__(self, VRP):
        self.VRP = VRP

    def reset_solution(self):
        for depot in self.VRP.depots:
            depot.path = []
            depot.route_cost = 0.0

        for vertice in self.VRP.vertices:
            vertice.visited = False

    def get_distance(self, node1, node2):
        distance = np.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)

        return distance

    def assign_vertices_to_depot(self):
        groups = {}
        for i in range(len(self.VRP.depots)):
            groups[i] = []

        for vertice in self.VRP.vertices:
            shortest_distance = float("inf")
            closest_depot = None
            for depot in self.VRP.depots:
                distance = self.get_distance(node1=depot, node2=vertice)
                if distance < shortest_distance:
                    shortest_distance = distance
                    closest_depot = depot.index
            groups[closest_depot].append(vertice)

        for depot in self.VRP.depots:
            depot.assigned_vertices = groups[depot.index]

    def get_nearest_neighbour(self, node, group):
        min_distance = float("inf")
        nearest_neighbour = None
        for vertice in group:
            if vertice.visited == False:
                distance = self.get_distance(node1=node, node2=vertice)
                if min_distance > distance:
                    min_distance = distance
                    nearest_neighbour = vertice
        return nearest_neighbour, min_distance

    def get_route_cost(self, depot):
        total_route = 0.0
        for i in range(len(depot.path) - 1):
            total_route += self.get_distance(node1=depot.path[i], node2=depot.path[i + 1])
        return round(total_route)

    def solve_nearest_neighbour(self):
        for depot in self.VRP.depots:
            depot.path.append(depot)
            next_node = depot
            for i in range(len(depot.assigned_vertices)):
                next_node, _ = self.get_nearest_neighbour(node=next_node, group=depot.assigned_vertices)
                depot.path.append(next_node)
                next_node.visited = True
            depot.path.append(depot)
            depot.route_cost = self.get_route_cost(depot)

    def get_insertion_distance(self, node1, middle_node, node2):
        existing_distance = self.get_distance(node1=node1, node2=node2)
        distance_to_new_node = self.get_distance(node1=node1, node2=middle_node)
        distance_from_new_node = self.get_distance(node1=middle_node, node2=node2)
        insertion_distance = distance_to_new_node + distance_from_new_node - existing_distance

        return insertion_distance

    def insert_node_into_cycle(self, cycle: list, new_node):
        min_cycle_distance = float("inf")
        for i in range(len(cycle) - 1):
            insertion_distance = self.get_insertion_distance(node1=cycle[i], middle_node=new_node, node2=cycle[i + 1])
            if insertion_distance < min_cycle_distance:
                min_cycle_distance = insertion_distance
                insertion_index = i + 1
        cycle.insert(insertion_index, new_node)
        new_node.visited = True
        return cycle

    def solve_nearest_insertion(self):
        for depot in self.VRP.depots:
            cycle = [depot, depot]
            for _ in range(len(depot.assigned_vertices)):
                cycle_nearest_neighbour = None
                nearest_neighbour_distance = float("inf")
                for node in cycle:
                    node_nearest_neighbour, distance = self.get_nearest_neighbour(
                        node=node, group=depot.assigned_vertices
                    )
                    if distance < nearest_neighbour_distance:
                        cycle_nearest_neighbour = node_nearest_neighbour
                        nearest_neighbour_distance = distance
                cycle = self.insert_node_into_cycle(cycle=cycle, new_node=cycle_nearest_neighbour)
            depot.path = cycle
            depot.route_cost = self.get_route_cost(depot=depot)

    def run_min_max(self):
        longest_route_depot = None
        longest_path = 0.0
        for depot in self.VRP.depots:
            if depot.route_cost > longest_path:
                longest_route_depot = depot
                longest_path = depot.route_cost

        distances = []
        for i in range(1, len(longest_route_depot.path) - 1):
            saved_distance = self.get_insertion_distance(
                node1=longest_route_depot.path[i - 1],
                middle_node=longest_route_depot.path[i],
                node2=longest_route_depot.path[i + 1],
            )
            distances.append({"vertice": longest_route_depot.path[i], "distance": saved_distance})
        sorted_distances = sorted(distances, key=lambda dictionary: dictionary["distance"])

        temp_path = [longest_route_depot]
        temp_assigned_vertices = []
        longest_saved_distance = sorted_distances.pop()["vertice"]

        for i in range(len(longest_route_depot.path)):
            vertice = longest_route_depot.path[i]
            if type(vertice) is not Depot and vertice != longest_saved_distance:
                temp_path.append(vertice)
                temp_assigned_vertices.append(vertice)
        temp_path.append(longest_route_depot)


# """
# Find longest path (depot)
# Make list of saved distance if vertice will be deleted
# Sort that list

# for vertice in sorted_list:
#     take out vetice of longest path
#     put vertice into another path
#     if the total distance will be better:
#         save both paths
#     else:
#         reset paths as in beggining of loop
# """
