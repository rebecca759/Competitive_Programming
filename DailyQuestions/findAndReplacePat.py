class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        
        for word in words:
            pat_dict = {}
            word_dict = {}
            i = 0
            match = True
            
            while i < len(word) and i < len(pattern):
                if word[i] in word_dict:
                    if word_dict[word[i]] != pattern[i]:
                        match = False
                        break
                
                elif pattern[i] in pat_dict:
                    print(word)
                    if pat_dict[pattern[i]] != word[i]:
                        match = False
                        break
                else:
                    pat_dict[pattern[i]] = word[i]
                    word_dict[word[i]] = pattern[i]
                    
                i += 1
                
            if match:
                res.append(word)
                
        return res
