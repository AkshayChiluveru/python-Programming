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

    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            return max(left_height, right_height) + 1


tree = BinaryTree()
tree.root = tree.create_tree()

height = tree.height(tree.root)
print("Height of the tree:", height)
