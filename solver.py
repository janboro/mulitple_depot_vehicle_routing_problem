import numpy as np
from data_types.coordinates import Depot, Vertice
from plots import Plotter


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

    def get_depot_with_longest_route(self):
        longest_route_depot = None
        longest_path = 0.0
        for depot in self.VRP.depots:
            if depot.route_cost > longest_path:
                longest_route_depot = depot
                longest_path = depot.route_cost
        return longest_route_depot, longest_path

    def get_vertice_potential_saved_distance(self, depot: Depot):
        distances = []
        for i in range(1, len(depot.path) - 1):
            saved_distance = self.get_insertion_distance(
                node1=depot.path[i - 1],
                middle_node=depot.path[i],
                node2=depot.path[i + 1],
            )
            distances.append({"vertice": depot.path[i], "distance": saved_distance})
        sorted_distances = sorted(distances, key=lambda dictionary: dictionary["distance"])
        return sorted_distances

    def remove_vertice_from_assigned_vertices(self, depot, vertice_to_remove):
        for i in range(len(depot.assigned_vertices)):
            if depot.assigned_vertices[i] is vertice_to_remove:
                del depot.assigned_vertices[i]
                break

    def remove_vertice_from_path(self, depot, vertice_to_remove):
        for i in range(len(depot.path)):
            if depot.path[i] is vertice_to_remove:
                del depot.path[i]
                break

    def get_path_to_insert(self, node_to_insert, longest_route_depot):
        shortest_distance = float("inf")
        depot_to_insert = None
        index_to_insert = None
        for depot in self.VRP.depots:
            if depot is not longest_route_depot:
                for i in range(len(depot.path) - 1):
                    insertion_distance = self.get_insertion_distance(
                        node1=depot.path[i],
                        middle_node=node_to_insert,
                        node2=depot.path[i + 1],
                    )
                    if insertion_distance < shortest_distance:
                        depot_to_insert = depot
                        index_to_insert = i
        return depot_to_insert, index_to_insert

    def run_min_max(self, TSP_function):
        """
        The point of min max is minimize the longest route, so in short it tries to make the routes of similar length
        """
        longest_route_depot, longest_route = self.get_depot_with_longest_route()
        sorted_distances = self.get_vertice_potential_saved_distance(depot=longest_route_depot)
        for _ in range(len(sorted_distances)):
            vertice_to_move = sorted_distances.pop()["vertice"]

            temp_old_depot_path = longest_route_depot.path.copy()
            temp_old_depot_assigned_vertices = longest_route_depot.assigned_vertices.copy()
            temp_old_depot_cost = longest_route_depot.route_cost

            self.remove_vertice_from_path(depot=longest_route_depot, vertice_to_remove=vertice_to_move)
            self.remove_vertice_from_assigned_vertices(depot=longest_route_depot, vertice_to_remove=vertice_to_move)

            depot_to_insert_vertice, insertion_index = self.get_path_to_insert(
                node_to_insert=vertice_to_move, longest_route_depot=longest_route_depot
            )
            temp_new_depot_path = depot_to_insert_vertice.path.copy()
            temp_new_depot_assigned_vertices = depot_to_insert_vertice.assigned_vertices.copy()
            temp_new_depot_cost = depot_to_insert_vertice.route_cost

            depot_to_insert_vertice.path.insert(insertion_index, vertice_to_move)
            depot_to_insert_vertice.assigned_vertices.append(vertice_to_move)

            self.reset_solution()
            TSP_function()
            new_longest_route_depot, new_longest_route = self.get_depot_with_longest_route()
            if new_longest_route < longest_route:
                if new_longest_route_depot is not longest_route_depot:
                    break
            else:
                longest_route_depot.path = temp_old_depot_path
                longest_route_depot.route_cost = temp_old_depot_cost
                longest_route_depot.assigned_vertices = temp_old_depot_assigned_vertices

                depot_to_insert_vertice.path = temp_new_depot_path
                depot_to_insert_vertice.route_cost = temp_new_depot_cost
                depot_to_insert_vertice.assigned_vertices = temp_new_depot_assigned_vertices
