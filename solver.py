import numpy as np


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

    def insert_node_into_cycle(self, cycle: list, new_node):
        min_cycle_distance = float("inf")
        insertion_point = None
        for i in range(len(cycle) - 1):
            existing_distance = self.get_distance(node1=cycle[i], node2=cycle[i + 1])
            distance_to_new_node = self.get_distance(node1=cycle[i], node2=new_node)
            distance_from_new_node = self.get_distance(node1=new_node, node2=cycle[i + 1])
            insertion_distance = distance_to_new_node + distance_from_new_node - existing_distance

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
