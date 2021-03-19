class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:            
        paragraph_lst = paragraph.split(' ')
        word_dict = {}
        
        words = []
        index = 0
        
        freq_word = ''
        max_freq = 0
        
        for j in range(len(paragraph_lst)):
            word = paragraph_lst[j]
            
            for i in range(len(word)):
                if i != len(word)-1 and word[i] == ',':
                    words = word.split(',')
                    index = j
                    break
                    
        if len(words) > 0:
            paragraph_lst.pop(index)
            
            for word in words:
                if len(word) > 0:
                    paragraph_lst.append(word)
         
        
        for i in range(len(paragraph_lst)):
            paragraph_lst[i] = paragraph_lst[i].lower()
            
            word_lst = list(paragraph_lst[i])
            
            for char in word_lst:
                if not char.isalpha() or char == 0:
                    word_lst.remove(char)
                   
  
            paragraph_lst[i] = ''.join(word_lst)
                
        for word in paragraph_lst:
            if len(word) == 0:
                continue
            
            if word in word_dict:
                word_dict[word] += 1
    
            else:
                word_dict[word] = 1
                
        for word in word_dict:
            if word_dict[word] > max_freq and word not in banned:
                max_freq = word_dict[word]
                freq_word = word
               
        print(word_dict)
        
        return freq_word
