def repeatedString(s, n):
    count = 0
    even_repetitions = n // len(s)
    remaining = n % len(s)
    remaining_count = 0
    
    for i in range(len(s)):
        if s[i] == 'a':
            count += 1
        
        if i < remaining:
            if s[i] == 'a':
                remaining_count += 1
    
                
    reptetitions = (even_repetitions * count) + remaining_count
    
    return reptetitions
