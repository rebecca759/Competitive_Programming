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

    return int(summ[::-1])

def calculate_sum_negative(a,b):
    if int(a) < 0 and int(b) < 0:
        numA = str(abs(int(a)))
        numB = str(abs(int(b)))
        return -calculate_sum(numA,numB)

    if int(a) > 0 and int(b) > 0:
        return calculate_sum(a,b)

    negative_num = a if int(a) < 0 else b
    positive_num = a if int(a) > 0 else b

    if -int(negative_num) > int(positive_num):
        return -subtract(str(-int(negative_num)), positive_num)

    elif -int(negative_num) < int(positive_num):
        return subtract(positive_num,str(-int(negative_num)))

    elif -int(negative_num) == int(positive_num):
        return 0
        
def subtract(positive,negative):
    list_pos = list(positive)
    list_neg = list(negative)

    posInd = len(list_pos)-1
    negInd = len(list_neg)-1

    borrow = 10
    result = ''

    while posInd >= 0 or negInd >= 0:
        num_pos = int(list_pos[posInd]) if posInd >= 0 else 0
        num_neg = int(list_neg[negInd]) if negInd >= 0 else 0
        
        n = 0
        
        if num_pos < num_neg:
            n = (num_pos + borrow) - num_neg
            list_pos[posInd - 1] = str(int(list_pos[posInd - 1])-1)

        else:
            n = num_pos - num_neg

        result += str(n)
        
        posInd -= 1
        negInd -= 1

    return int(result[::-1])
    
 
print(calculate_sum_negative('-999','100'))
