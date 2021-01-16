# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    current = head
    
    while current:
        node = head
        while node != current:
            if current.next == node:
                return 1
            node = node.next
        
        current = current.next
    
    return 0
