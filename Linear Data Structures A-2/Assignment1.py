# Delete the elements in an linked list whose sum is equal to zero

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_zero_sum(head):
    dummy = Node(0)
    dummy.next = head
    prefix_sum = 0
    prefix_sums = {}
    
    curr = dummy
    while curr:
        prefix_sum += curr.data
        if prefix_sum in prefix_sums:
            prev = prefix_sums[prefix_sum].next
            temp_sum = prefix_sum
            while prev != curr:
                temp_sum += prev.data
                del prefix_sums[temp_sum]
                prev = prev.next
            prefix_sums[prefix_sum].next = curr.next
        else:
            prefix_sums[prefix_sum] = curr
        curr = curr.next
    
    return dummy.next
