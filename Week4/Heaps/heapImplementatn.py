#Python3 implementation of Min heap

import sys

class MinHeap:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1

    #Function to return the position of
    #Parent for the node currently at pos
    def parent(self,pos):
        return (pos)//2

    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self,pos):
        return (2*pos)+1

    # Function to return the position of
    # the right child for the node currently
    # at pos
    def rightChild(self,pos):
        return (2*pos)+2


    #Function to return true if the passed node is a leaf node
    def isLeaf(self,pos):
        if pos >= (self.size//2) and pos <= self.size:
            return True
        
        return False

    #Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    #Function to heapify the node at pos
    def minHeapify(self, pos):
        




    

    

        

        
