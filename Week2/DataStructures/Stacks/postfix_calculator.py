def evalRPN(tokens):
        stack = []
        
        for op in tokens:
            if not (op in '+-*/'):
                stack.append(op)
                
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                
                operator = op
                
                result = evaluate(op1,op2,operator)
                stack.append(result)
        
        return stack.pop()         
                
def evaluate(op1,op2,operator):
    if operator == '+':
        return int(op1)+int(op2)
    elif operator == '-':
        return int(op1)-int(op2)
    elif operator == '*':
        return int(op1)*int(op2)
    elif operator == '/':
        return int(int(op1)/int(op2))

        
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))   

