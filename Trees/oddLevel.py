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

    def print_odd_level_nodes(self, node, level):
        if node is None:
            return
        if level % 2 != 0:
            print(node.data, end=" ")
        self.print_odd_level_nodes(node.left, level + 1)
        self.print_odd_level_nodes(node.right, level + 1)


tree = BinaryTree()
tree.root = tree.create_tree()

print("Nodes at odd levels:")
tree.print_odd_level_nodes(tree.root, 1)
print()
