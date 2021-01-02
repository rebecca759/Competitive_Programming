def calculate_sum(a,b):
    indA = len(a)-1
    indB = len(b)-1

    summ = ''
    carry = 0

    while indA >= 0 or indB >= 0:
        num1 = int(a[indA]) if indA >= 0 else 0
        num2 = int(b[indB]) if indB >= 0 else 0
        
        n = (num1 + num2 + carry) % 10
        carry = (num1 + num2 + carry) // 10
        
        summ += str(n)

        if indA > -1:
            indA -= 1

        if indB > -1:
            indB -= 1

    if carry:
        summ += str(carry)

    return summ[::-1]


def multiply_positives(a,b):
    maxx = a if len(a) >= len(b) else b
    minn = a if len(a) < len(b) else b

    indMax = len(maxx)-1
    indMin = len(minn)-1

    count = 0
    total_sum = ''

    while count < len(minn):
        indMax = len(maxx)-1
        
        current_mul = 0

        carry = 0
        current_sum = ''

        num2 = int(minn[indMin]) if indMin >= 0 else 0
        
        while indMax >= 0:
            num1 = int(maxx[indMax])

            m = (num1 * num2 + carry) % 10
            carry = (num1 * num2 + carry) // 10

            current_sum += str(m)

            indMax -= 1

        if carry:
            current_sum = str(carry) + current_sum[::-1]

        else:
            current_sum = current_sum[::-1]

        total_sum = calculate_sum(current_sum+('0'*count),('0'*count)+total_sum)
    
        indMin -= 1
            
        count += 1

    return int(total_sum)

def multiply(a,b):
    if int(a) >= 0 and int(b) >= 0:
        return multiply_positives(a,b)

    elif (int(a) < 0) and (int(b) > 0):
        a = str(abs(int(a)))
        return -multiply_positives(a,b)
        

    elif (int(a) > 0) and (int(b) < 0):
        b = str(abs(int(b)))
        return -multiply_positives(a,b)

    elif (int(a) < 0) and (int(b) < 0):
        a = str(abs(int(a)))
        b = str(abs(int(b)))

        return multiply_positives(a,b)

print(multiply('1000029364','999999999'))
            

            
