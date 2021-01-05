def divide(a,b):
    dividend = int(a)
    divisor = int(b)
    
    if divisor == 0:
        return "Undefined: division by zero"

    elif dividend == divisor:
        return 1

    elif divisor == 1:
        return dividend

    elif dividend % divisor == 0:
        return _divide(str(dividend),str(divisor))

    elif dividend % divisor != 0:
        return divide_frac(str(dividend),str(divisor))

def _divide(a,b):
    remainder = 0
    quotient = ''
    
    divisor = int(b)
    dividend = a

    dividend_part = a[0]
    
    i = 1

    count = 0
    zeros = False

    while True:
        if int(dividend_part) < divisor:
            while int(dividend_part) < divisor and i < len(a):
                if int(dividend_part) == 0 and a[i] == '0':
                    zeros = True
                    quotient += '0'
                dividend_part += a[i]
                i += 1
                
                if quotient != '' and not zeros:
                    count += 1

                    if count >= 2:
                        quotient += '0'

                zeros = False

        if int(dividend_part) == 0:
            break
       
        dividend_num = int(dividend_part)
        
        q = dividend_num // divisor
        quotient += str(q)

        remainder = dividend_num - (divisor * q)
        dividend_part = str(remainder)

        count = 0

    return int(quotient)

def divide_frac(a,b):
    remainder = 0
    quotient = ''
    
    divisor = int(b)
    dividend = a

    dividend_part = a[0]
    
    i = 1

    count = 0
    zeros = False

    while True:
        if int(dividend_part) < divisor:
            while int(dividend_part) < divisor and i < len(a):
                if int(dividend_part) == 0 and a[i] == '0':
                    zeros = True
                    quotient += '0'
                dividend_part += a[i]
                i += 1
                
                if quotient != '' and not zeros:
                    count += 1

                    if count >= 2:
                        quotient += '0'

                zeros = False

        if int(dividend_part) == 0:
            break

        if int(dividend_part) < divisor:
            if quotient == '':
                quotient += '0.'

            else:
                if '.' not in quotient:
                    quotient += '.'
                
            dividend_part += '0'
       
        dividend_num = int(dividend_part)
        
        q = dividend_num // divisor
        quotient += str(q)

        remainder = dividend_num - (divisor * int(quotient[-1]))
        dividend_part = str(remainder)

        count = 0

        if len(quotient) > 15:
            return float(quotient)

    return float(quotient)


print(divide(9,8989))
