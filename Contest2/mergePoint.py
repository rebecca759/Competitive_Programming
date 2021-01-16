# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    stack1 = []
    stack2 = []
    mg = 0
    
    while head1:
        stack1.append(head1)
        head1 = head1.next
        
    while head2:
        stack2.append(head2)
        head2 = head2.next
        
    while True:
        if not stack1 or not stack2:
            break
            
        merge_point1 = stack1.pop()
        merge_point2 = stack2.pop()

        if merge_point1 == merge_point2:
            mg = merge_point1.data

        else:
            break
              
    return mg
    
