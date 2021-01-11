def isValid(s):
    stack = []

    for c in s:
        if c == '[' or c == '(' or c == '{':
            stack.append(c)
            
        else:
            if len(stack) == 0:
                return False
            
            open_paren = stack.pop()
            
            if not matches(open_paren,c):
                return False
            
    if len(stack) > 0:
        return False
            
    return True
    
def matches(p1,p2):
    if p1 == '(' and p2 == ')':
        return True
    
    elif p1 == '[' and p2 == ']':
        return True
    
    elif p1 == '{' and p2 == '}':
        return True
    
    else:
        return False

print(isValid('()(){{}'))
