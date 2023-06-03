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

    def print_leaves(self, node):
        if node is None:
            return
        if node.left is None and node.right is None:
            print(node.data, end=" ")
        self.print_leaves(node.left)
        self.print_leaves(node.right)


tree = BinaryTree()
tree.root = tree.create_tree()

print("Leaves in the tree:")
tree.print_leaves(tree.root)
print()
