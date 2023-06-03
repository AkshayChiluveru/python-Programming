class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def create_tree(self):
        data = input("Enter the value of the root node : ")
        if data.lower() == 'none':
            return None
        root = Node(int(data))
        print("Enter the left subtree of", data)
        root.left = self.create_tree()
        print("Enter the right subtree of", data)
        root.right = self.create_tree()
        return root

    def sum_left_leaves(self, node):
        if node is None:
            return 0
        if node.left is not None and node.left.left is None and node.left.right is None:
            return node.left.data + self.sum_left_leaves(node.right)
        return self.sum_left_leaves(node.left) + self.sum_left_leaves(node.right)

# Example usage:
tree = BinaryTree()
tree.root = tree.create_tree()

left_leaves_sum = tree.sum_left_leaves(tree.root)
print("Sum of left leaves:", left_leaves_sum)
