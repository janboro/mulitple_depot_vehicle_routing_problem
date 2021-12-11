class MDVRPSolver:
    def __init__(self, problem_map):
        self.problem_map = problem_map

    def get_distance(self, depo, vertice):
        distance = (depo.x - vertice.x) ** 2
        +((depo.y - vertice.y) ** 2)

        return distance

    def assign_vertices_to_depo(self):
        for vertice in self.problem_map.vertices:
            shortest_distance = float("inf")
            closest_depo = None
            for depo in self.problem_map.depots:
                distance = self.get_distance(depo=depo, vertice=vertice)
                if distance < shortest_distance:
                    shortest_distance = distance
                    closest_depo = depo.index
            vertice.assigned_depo = closest_depo
