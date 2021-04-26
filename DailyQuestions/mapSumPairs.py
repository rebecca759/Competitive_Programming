class TrieNode:
    def __init__(self,value):
        self.value = value
        self.children = {}
        self.endsHere = False

class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.map = {}
        self.root = TrieNode('')

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val
        
        cur_root = self.root
        
        for i in range(len(key)):
            char = key[i]
            
            if char not in cur_root.children:
                cur_root.children[char] = TrieNode(char)
                
            cur_root = cur_root.children[char]
                
            if i == len(key)-1:
                cur_root.endsHere = True

    def sum(self, prefix: str) -> int:
        total = 0
        queue = deque()
        
        cur_root = self.root
        cur_word = prefix
        
        for i in range(len(prefix)):
            char = prefix[i]
            if char not in cur_root.children:
                return 0
            cur_root = cur_root.children[char]
  
        queue.append((cur_root,cur_word))
        
        while queue:
            cur_root,cur_word = queue.popleft()
            
            if cur_root.endsHere: 
                total += self.map[cur_word]
            
            for char in cur_root.children:
                queue.append((cur_root.children[char],cur_word+char))
                
        return total


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
