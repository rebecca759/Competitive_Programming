class TrieNode:
    def __init__(self,value):
        self.value = value
        self.children = {}
        self.endsHere = False
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('')  

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_root = self.root
        
        for i in range(len(word)):
            char = word[i]
            
            if char not in cur_root.children:
                cur_root.children[char] = TrieNode(char)
                
            cur_root = cur_root.children[char]
            
            if i == len(word)-1:
                cur_root.endsHere = True
                


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_root = self.root
        
        for char in word:
            if char not in cur_root.children:
                return False
            
            cur_root = cur_root.children[char]
            
        return cur_root.endsHere
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_root = self.root
        
        for char in prefix:
            if char not in cur_root.children:
                return False
            
            cur_root = cur_root.children[char]
            
        return True
       

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
