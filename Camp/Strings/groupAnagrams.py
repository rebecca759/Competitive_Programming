class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_2 = []
        word_dict = {}
        
        result = []
        
        for word in strs:
            strs_2.append((''.join(sorted(list(word)))))
            
        for word in strs_2:
            if word in word_dict:
                continue
                
            word_dict[word] = []
            
        for i in range(len(strs_2)):
            word = strs_2[i]
            
            word_dict[word].append(strs[i])
            
        for word in word_dict:
            result.append(word_dict[word])
            
        return result
