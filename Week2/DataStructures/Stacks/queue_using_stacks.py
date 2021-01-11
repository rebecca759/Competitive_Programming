class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.front = 0
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if len(self.stack1) == 0:
            self.front = x
            
        self.stack1.append(x)
        
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.stack2) == 0:
            while (len(self.stack1) > 0):
                self.stack2.append(self.stack1.pop())
                
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not (self.stack2 == []):
            return self.stack2[-1]
        
        return self.front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return (self.stack1 == []) and (self.stack2 == [])

q = MyQueue()
q.push(1)
q.push(2)
q.push(3)
print(q.pop())
print(q.empty())
