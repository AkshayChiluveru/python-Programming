from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def count_trees(self):
        visited = [False] * self.V
        count = 0

        for v in range(self.V):
            if not visited[v]:
                if self.dfs_util(v, visited):
                    count += 1

        return count

    def dfs_util(self, v, visited):
        visited[v] = True

        for neighbor in self.adj_list[v]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

        return True


V = int(input("Enter the number of vertices: "))
graph = Graph(V)

E = int(input("Enter the number of edges: "))
for _ in range(E):
    u, v = map(int, input("Enter the vertices of an edge: ").split())
    graph.add_edge(u, v)

trees_count = graph.count_trees()
print("Number of trees in the forest:", trees_count)
