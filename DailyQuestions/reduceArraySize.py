class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count_dict = defaultdict(int)
        count_arr = []
        count = 0
        removed = len(arr)
        half = len(arr)//2
        
        for num in arr:
            count_dict[num] += 1
            
        for num in count_dict:
            count_arr.append((num,count_dict[num]))
            
        count_arr = sorted(count_arr,key= lambda x: x[1])
        
        for i in range(len(count_arr)-1,-1,-1):
            removed -= count_arr[i][1]
            count += 1
            if removed <= half:
                return count
