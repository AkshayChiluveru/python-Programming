class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(self.V)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def is_cyclic_util(self, vertex, visited, rec_stack):
        visited[vertex] = True
        rec_stack[vertex] = True

        for neighbor in self.adj_list[vertex]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[vertex] = False
        return False

    def is_cyclic(self):
        visited = [False] * self.V
        rec_stack = [False] * self.V

        for vertex in range(self.V):
            if not visited[vertex]:
                if self.is_cyclic_util(vertex, visited, rec_stack):
                    return True

        return False



V = int(input("Enter the number of vertices: "))
graph = Graph(V)

E = int(input("Enter the number of edges: "))
for _ in range(E):
    u, v = map(int, input("Enter the vertices of an edge: ").split())
    graph.add_edge(u, v)

if graph.is_cyclic():
    print("The graph contains a cycle.")
else:
    print("The graph does not contain a cycle.")
