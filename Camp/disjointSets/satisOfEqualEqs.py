class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        letters = [x for x in range(26)]
        sizes = [1] * 26
        
        def find(num):
            if letters[num] == num:
                return num
            
            letters[num] = find(letters[num])
            return letters[num]
        
 
        for equation in equations:
            x = ord(equation[0]) - ord('a')
            y = ord(equation[-1]) - ord('a')

            if equation[1] == '=':                
                num1 = find(x)
                num2 = find(y)
                
                if sizes[num1] >= sizes[num2]:
                    letters[num2] = letters[num1]
                    sizes[num1] += sizes[num2]
                    
                else:
                    letters[num1] = letters[num2]
                    sizes[num2] += sizes[num1]

        for equation in equations:
            x = ord(equation[0]) - ord('a')
            y = ord(equation[-1]) - ord('a')

            if equation[1] == '!' and find(x) == find(y):
                return False
       
        return True
            
