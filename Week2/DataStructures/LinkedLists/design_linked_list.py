class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.next = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        
        current = self
        count = 0
        
        if current.val and index == 0:
            return current.val
        
        while current.val:
            current = current.next
            count += 1
            
            if count == index:
                return current.val
            
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        
        if not self.val:
            self.val = val
            
        else:
            self.next = self
            self.val = val


ll = MyLinkedList()
ll.addAtHead(2)
ll.addAtHead(1)
print(ll.get(1))
