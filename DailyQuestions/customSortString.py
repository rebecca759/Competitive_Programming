class Solution:
    def customSortString(self, order: str, str: str) -> str:
        word_dict = collections.Counter(str)
        new_str = ''
        
        for char in order:
            if char in word_dict:
                for i in range(word_dict[char]):
                    new_str += char
                word_dict.pop(char)
            
        for char in word_dict:
            for i in range(word_dict[char]):
                new_str += char
                
        return new_str
