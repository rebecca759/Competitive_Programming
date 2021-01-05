def twoStacks(x, a, b):
    for a_index, value in enumerate(a):
        if value > x:
            a_index -= 1
            break
        
        x -= value
        
    max_picks = a_index + 1

    
    
    # try filling b removing from a when necessary
    for b_index, value in enumerate(b):
        print(x)
        while value > x and a_index >= 0:
            x += a[a_index]
            a_index -= 1
        if value > x:
            return max_picks
        max_picks = max(max_picks, b_index + a_index + 2)
        x -= value
        
    return max_picks


print(twoStacks(10,[4,2,4,6,1],[2,1,8,5]))
