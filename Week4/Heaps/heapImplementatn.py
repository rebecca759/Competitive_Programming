import sys

class MinHeap:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1

    def parent(self,pos):
        return (pos-1)//2

    def leftChild(self,pos):
        return (2*pos)+1

    def rightChild(self,pos):
        return (2*pos)+2

    def isLeaf(self,pos):
        if (2*pos)+1 < self.size-1:
            return True

        return False

    

        

        
