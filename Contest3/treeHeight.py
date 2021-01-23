# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def height(root):
    return _height(root,0,0)
    
def _height(root,h1,h2):
    if not root.left and not root.right:
        return max(h1,h2)

    if root.left:
        h1 = 1 + _height(root.left,h1,0)
    
    if root.right:
        h2 = 1 + _height(root.right,0,h2)
        
        
    return max(h1,h2)
        
