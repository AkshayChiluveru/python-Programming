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

    def max_level_sum(self, root):
        if root is None:
            return 0
        queue = deque()
        queue.append(root)
        max_sum = float('-inf')
        while queue:
            level_sum = 0
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.data
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            max_sum = max(max_sum, level_sum)
        return max_sum



tree = BinaryTree()
tree.root = tree.create_tree()

max_sum = tree.max_level_sum(tree.root)
print("Maximum level sum in the binary tree:", max_sum)
