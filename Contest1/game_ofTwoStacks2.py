def twoStacks(x,a,b):
    maxnum = total = i = j = 0

    #Take as many elements from stack A

    while i < len(a) and total + a[i] <= x:
        total += a[i]
        i += 1
        maxnum += 1

    #Take elements from stack B
    while j < len(b) and i >= 0:
        total += b[j]
        j += 1

        #remove taken elements from stack A
        while i > 0 and total > x:
            i -= 1
            total -= a[i]

        #update maxnum
        if total <= x and maxnum < i+j:
             maxnum = i + j

    return maxnum
