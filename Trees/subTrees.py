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

    def count_subtrees_with_sum(self, node, target_sum):
        if node is None:
            return 0
        count = 0
        if self.subtree_sum(node) == target_sum:
            count += 1
        count += self.count_subtrees_with_sum(node.left, target_sum)
        count += self.count_subtrees_with_sum(node.right, target_sum)
        return count

    def subtree_sum(self, node):
        if node is None:
            return 0
        return node.data + self.subtree_sum(node.left) + self.subtree_sum(node.right)



tree = BinaryTree()
tree.root = tree.create_tree()

target_sum = int(input("Enter the target sum: "))
count_subtrees = tree.count_subtrees_with_sum(tree.root, target_sum)
print("Count of subtrees with sum", target_sum, ":", count_subtrees)
