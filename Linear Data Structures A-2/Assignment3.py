# Merge a linked list into another linked list at alternate positions.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_linked_lists(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    
    curr1 = head1
    curr2 = head2
    
    while curr1 and curr2:
        next1 = curr1.next
        next2 = curr2.next
        
        curr1.next = curr2
        curr2.next = next1
        
        curr1 = next1
        curr2 = next2
    
    return head1
