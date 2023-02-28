class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1 for _ in range(k)]
        self.front = -1
        self.rear = -1
        self.size,self.k = 0,k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        r = (self.rear+1)%self.k
        self.queue[r] = value
        self.rear = r
        if self.front == -1:
            self.front += 1
        self.size += 1
        return True

    def deQueue(self) -> bool:
        print(self.queue,self.front)
        if self.isEmpty():
            return False
        f = (self.front+1)%self.k
        self.queue[self.front] = -1
        self.front = f
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0
        
    def isFull(self) -> bool:
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()