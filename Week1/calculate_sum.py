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

 
<<<<<<< HEAD:Week1/calculate_sum.py

print(calculate_sum('9999','9999999'))










    
=======
print(calculate_sum('9999','9999999'))
>>>>>>> 78ee5ff442cb929367d49dd533112532c2c16a46:day1/calculate_sum.py
