# Reverse a linked list in groups of given size

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list_groups(head, k):
    if not head or k <= 1:
        return head
    
    dummy = Node(0)
    dummy.next = head
    prev_group_end = dummy
    
    while True:
        curr_group_start = prev_group_end.next
        curr = curr_group_start
        prev = None
        i = 0
        
        while i < k and curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            i += 1
        
        prev_group_end.next = prev
        curr_group_start.next = curr
        
        if not curr:
            break
        
        prev_group_end = curr_group_start
    
    return dummy.next
