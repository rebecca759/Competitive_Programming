from collections import deque
class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = deque()
        self.queue2 = deque()
        self.top_elem = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.appendleft(x)
        self.top_elem = x
        
        
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        
        while len(self.queue1) > 1:
            self.top_elem = self.queue1.pop()
            self.queue2.appendleft(self.top_elem)
            
        temp = self.queue1
        self.queue1 = self.queue2
        self.queue2 = temp
        
        
        return self.queue2.pop()
        
        
    def top(self) -> int:
        """
        Get the top element.
        """
        return self.top_elem
        
        
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1) == 0        
        

stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.pop())
print(stack.pop())
print(stack.empty())
