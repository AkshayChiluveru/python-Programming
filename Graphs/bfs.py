from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def count_nodes_at_level(root, level):
    if root is None:
        return 0

    queue = deque()
    queue.append(root)
    current_level = 0
    count = 0

    while queue:
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()
            if current_level == level:
                count += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        current_level += 1

    return count


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

level = int(input("Enter the level to count nodes from: "))
count = count_nodes_at_level(root, level)
print("Number of nodes at level", level, ":", count)
