def bonAppetit(bill, k, b):
    b_charged = b
    total_cost = 0
    
    for i in range(len(bill)):
        if i == k:
            pass
        else:
            total_cost += bill[i]
            
    b_actual = total_cost // 2
    
    if b_charged == b_actual:
        print('Bon Appetit')
    
    elif b_charged > b_actual:
        print(b_charged - b_actual)
