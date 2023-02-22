class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        s = "".join(s.strip().split())
        stack = []

        def evaluate(num):
            nonlocal stack

            if stack and stack[-1] in "-+":
                op = stack.pop()
                if not stack or type(stack[-1]) != int:
                    stack.append(-num)
                else:
                    num1 = stack.pop()
                    if op == '-':
                        stack.append(num1-num)
                    else:
                        stack.append(num1+num)
            else:
                stack.append(num)
            
        for i,char in enumerate(s):
            if char == '(' or char in "+-":
                stack.append(char)
            
            elif char.isdigit():
                num = int(char)
                if stack and type(stack[-1]) == int:
                    num = int(str(stack.pop())+char)

                if i < len(s)-1 and s[i+1].isdigit():
                    stack.append(num)

                else:
                    evaluate(num)
                
            elif char == ')':
                num = stack.pop()
                stack.pop()    
                evaluate(num)

        return stack.pop()