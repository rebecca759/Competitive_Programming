# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def _print(self):
        current = self

        while current:
            print(current.val,end='')
            current = current.next

        print()
        

def reverseList(head: ListNode) -> ListNode:
    prev = None
    current = head
    
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    return prev._print()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

head._print()

reverseList(head)


