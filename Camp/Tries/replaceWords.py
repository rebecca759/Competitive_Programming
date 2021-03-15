class TrieNode:
    def __init__(self,value):
        self.value = value
        self.children = {}
        self.endsHere = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        #create trie with words in dictionary
        
        root = TrieNode('')
        
        sent_list = sentence.split(' ')
        
        for word in dictionary:
            #insert words to trie
            cur_root = root

            for i in range(len(word)):
                char = word[i]

                if char not in cur_root.children:
                    cur_root.children[char] = TrieNode(char)

                cur_root = cur_root.children[char]

            cur_root.endsHere = True
            
            
        for i in range(len(sent_list)):
            if sent_list[i][0] not in root.children:
                continue
                
            res_str = ''
            cur_root = root
            index = 0
            char = sent_list[i][index]
            
            while index < len(sent_list[i]) and char in cur_root.children:
                res_str += char
                cur_root = cur_root.children[char]
                
                if cur_root.endsHere:  
                    break
                    
                index += 1
                if (index < len(sent_list[i])):
                    char = sent_list[i][index]
                
            print(index)
            
            if cur_root.endsHere:
                sent_list[i] = res_str
   
                
        return " ".join(sent_list)

        
    
        
        
    
    
        
