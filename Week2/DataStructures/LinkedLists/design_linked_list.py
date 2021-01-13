class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        current = self.head
        count = 0
        
        if index == 0 and self.head:
            return self.head.val
        
        while current.next:
            current = current.next
            count += 1
            
            if count == index:
                return current.val
            
        return -1
    
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        
        
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        current = self.head
        
        if not self.head:
            self.head = new_node
            return
        
        while current.next:
            current = current.next
            
        current.next = new_node
    

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        new_node = Node(val)
        index_count = 0
        prev = None
        current = self.head
        found = False
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        while current.next:
            prev = current
            current = current.next
            index_count += 1
            
            if index_count == index:
                found = True
                break
            
        if found:
            prev.next = new_node
            new_node.next = current
            
        elif index_count+1 == index:
            current.next = new_node


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        
        index_count = 0
        prev = None
        current = self.head
        found = False
        
        if index == 0:
            self.head = self.head.next
            return
        
        while current.next:
            prev = current
            current = current.next
            index_count += 1
            
            if index_count == index:
                found = True
                break
                
        if found:
            prev.next = current.next
        

ll = MyLinkedList()
ll.addAtHead(1)
ll.addAtHead(2)
ll.addAtTail(6)
print(ll.get(1))
ll.addAtIndex(3,9)
ll.deleteAtIndex(2)
