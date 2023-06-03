from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(self.V)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def bfs(self, start):
        visited = [False] * self.V
        queue = deque()
        queue.append(start)
        visited[start] = True

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in self.adj_list[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True


V = int(input("Enter the number of vertices: "))
graph = Graph(V)

E = int(input("Enter the number of edges: "))
for _ in range(E):
    u, v = map(int, input("Enter the vertices of an edge: ").split())
    graph.add_edge(u, v)

start_vertex = int(input("Enter the starting vertex for BFS traversal: "))
print("BFS traversal:")
graph.bfs(start_vertex)
print()
