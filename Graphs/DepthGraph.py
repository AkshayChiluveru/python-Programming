class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(self.V)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def dfs_util(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")

        for neighbor in self.adj_list[vertex]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = [False] * self.V
        self.dfs_util(start, visited)



V = int(input("Enter the number of vertices: "))
graph = Graph(V)

E = int(input("Enter the number of edges: "))
for _ in range(E):
    u, v = map(int, input("Enter the vertices of an edge: ").split())
    graph.add_edge(u, v)

start_vertex = int(input("Enter the starting vertex for DFS traversal: "))
print("DFS traversal:")
graph.dfs(start_vertex)
print()
