def print_triangle(rows):
    for i in range(0,rows*2,2):
        print(' '*(rows-1),end = '')
        rows -= 1
        for j in range(i+1):
            print('*',end = '')

        print()


print_triangle(7)
