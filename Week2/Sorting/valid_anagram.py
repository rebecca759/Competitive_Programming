def isAnagram(s,t):
    letter_dict = {}
    
    for letter in s:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        
        else:
            letter_dict[letter] += 1
            
    for letter in t:
        if letter not in letter_dict:
            return False
        
        letter_dict[letter] -= 1
    
        if letter_dict[letter] < 0:
            return False
    
    for letter in letter_dict:
        if letter_dict[letter] > 0:
            return False
        
    return True

print(isAnagram('rat','tac'))
