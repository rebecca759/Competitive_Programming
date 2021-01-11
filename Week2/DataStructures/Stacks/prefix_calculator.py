#implement stack
class Stack:
    def __init__(self):
        self.items = []

    def push(self,data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []


def prefix_calculator(expression):
    expression = expression.split(' ')
    result = 0
    stack = Stack()

    for i in range(len(expression)-1,-1,-1):
        if not isOperand(expression[i]):
            stack.push(expression[i])

        else: 
            op1 = stack.pop()
            op2 = stack.pop()
            operator = expression[i]

            if operator == '+':
                stack.push(int(op1)+int(op2))

            elif operator == '-':
                stack.push(int(op1)-int(op2))

            elif operator == '*':
                stack.push(int(op1)*int(op2))

            elif operator == '/':
                stack.push(int(op1)/int(op2))

    return stack.pop()

def isOperand(e):
    return e in '+-*/'

print(prefix_calculator('- + * 2 3 * 5 4 9'))

