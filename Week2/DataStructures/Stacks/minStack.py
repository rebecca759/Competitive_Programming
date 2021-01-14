#Using two stacks

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.stack1 = []
        self.stack2 = []
        
        
    def push(self, x: int) -> None:
        self.stack1.append(x)
        
        if (len(self.stack2) == 0) or (self.stack2[-1] > x):
            self.stack2.append(x)
            
        else:
            self.stack2.append(self.stack2[-1])
        

    def pop(self) -> None:
        self.stack1.pop()
        
        self.stack2.pop()
        

    def top(self) -> int:
        return self.stack1[-1]
        

    def getMin(self) -> int:
        return self.stack2[-1]


#Using one stack
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        
    def push(self, x: int) -> None:
        if (len(self.stack) == 0) or (x < self.stack[-1][1]):
            self.stack.append((x,x))
            
        else:
            self.stack.append((x,self.stack[-1][1]))
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]

    
