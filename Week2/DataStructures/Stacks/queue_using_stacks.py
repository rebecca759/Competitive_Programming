class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
            
        self.stack1.append(x)
        
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack1.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack1[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.stack1 == []

q = MyQueue()
q.push(1)
q.push(2)
q.push(3)
print(q.pop())
print(q.empty())
