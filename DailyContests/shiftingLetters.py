class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        new_str = ''
        
        shift = sum(shifts)
        shift_val = 0
        add = shift

        
        for i in range(len(S)):
            char = S[i]

            if ord(char)+shift > 122:
                shift_val = 96 + (((ord(char)+shift) - 122)%26)

                
                if (((ord(char)+shift) - 122)%26) == 0:
                    shift_val = 122
                    
                
            else:
                shift_val = ord(char) + shift
                
            char = chr(shift_val)
            new_str += char
            
            shift -= shifts[i]
            
            
        return new_str
