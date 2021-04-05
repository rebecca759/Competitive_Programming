import heapq

size = input()
arr = []

for i in range(int(size)):
    elem = input()
    
    if len(elem.split(' ')) > 1:
        arr = elem.split(' ')
        break
    else:
        arr.append(int(elem))

heap = []
res = ''

for num in arr:
    heapq.heappush(heap,num)
    
for i in range(len(arr)):
    arr[i] = heapq.heappop(heap)
    
    if i != len(arr)-1:
        res += str(arr[i])+','
        
    else:
        res += str(arr[i])
    
print('['+res+']')
