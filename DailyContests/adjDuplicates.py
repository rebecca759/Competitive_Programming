class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        count_stack = []
        new_string = ''
        
        for letter in s:
            if len(count_stack) > 0 and count_stack[-1][0] != letter:
                count_stack.append((letter,1))
                
            elif len(count_stack) > 0 and count_stack[-1][0] == letter:
                count_stack.append((letter,count_stack[-1][1]+1))
                
            else:
                count_stack.append((letter,1))
                
            if count_stack[-1][1] == k:
                for i in range(k):
                    count_stack.pop()
                
            
                
        for l in count_stack:
            new_string += l[0]
            
        return new_string
        

                    
                
