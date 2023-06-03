import math

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

    def sum_perfect_binary_tree(self, node):
        if node is None:
            return 0
        height = math.floor(math.log2(self.count_nodes(node))) + 1
        total_nodes = (2 ** height) - 1
        return total_nodes * node.data

    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

# Example usage:
tree = BinaryTree()
tree.root = tree.create_tree()

perfect_tree_sum = tree.sum_perfect_binary_tree(tree.root)
print("Sum of all nodes in perfect binary tree:", perfect_tree_sum)
