class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.insert(0,x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        
        while len(self.queue1) > 0:
            self.queue2.append(self.queue1.pop())
            
        return self.queue2.pop()
        
        
    def top(self) -> int:
        """
        Get the top element.
        """
        while len(self.queue1) > 0:
            self.queue2.append(self.queue1.pop())
            
        return self.queue2[-1]
        
        
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1) == 0 and len(self.queue2) == 0
        
        

stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.pop())
print(stack.pop())
print(stack.empty())
