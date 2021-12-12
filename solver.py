class MDVRPSolver:
    def __init__(self, VRP):
        self.VRP = VRP

    def get_distance(self, node1, node2):
        distance = (node1.x - node2.x) ** 2
        +((node1.y - node2.y) ** 2)

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
        nearest_neighbour.visited = True
        return nearest_neighbour, min_distance

    def solve_NN(self):
        for depot in self.VRP.depots:
            next_node = depot
            for i in range(len(depot.assigned_vertices)):
                next_node, cost = self.get_nearest_neighbour(node=next_node, group=depot.assigned_vertices)
                depot.path.append(next_node)
                depot.route_cost += cost
