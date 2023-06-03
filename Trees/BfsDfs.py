from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def create_tree(self):
        data = input("Enter the value of the root node: ")
        if data.lower() == 'none':
            return None
        root = Node(int(data))
        print("Enter the left subtree of", data)
        root.left = self.create_tree()
        print("Enter the right subtree of", data)
        root.right = self.create_tree()
        return root

    def bfs(self):
        if self.root is None:
            return
        queue = deque()
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            print(node.data, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def dfs(self):
        if self.root is None:
            return
        stack = []
        stack.append(self.root)
        while stack:
            node = stack.pop()
            print(node.data, end=" ")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


tree = BinaryTree()
tree.root = tree.create_tree()

print("BFS traversal:")
tree.bfs()
print()

print("DFS traversal:")
tree.dfs()
print()
