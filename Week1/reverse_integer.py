def reverse(x):
    res = 0
    m = 0
    
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31
    
    while x:
        if x < 0:
            m = x % (- 10)
            x = int(x / 10)
            if (res < int(INT_MIN/10)) or (res == int(INT_MIN/10) and m < -8):
                return 0
            res = res * 10 + m
          
        else:
            m = x % 10
            x = x // 10
            if (res > INT_MAX/10) or (res == INT_MAX / 10 and m > 7):
                return 0
            res = res * 10 + m
            

    return res

print(reverse(-123))
