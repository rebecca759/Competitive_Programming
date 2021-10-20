#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
class RandomizedSet:

    def __init__(self):
        self.rand_dict = {}
        self.rand_list = []
        
    def insert(self, val: int) -> bool:
        if val in self.rand_dict:
            return False
        
        self.rand_dict[val] = len(self.rand_list)
        self.rand_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.rand_dict:
            return False

        ind = self.rand_dict[val]
        self.rand_dict.pop(val)
        #swap
        self.rand_list[ind],self.rand_list[-1] = self.rand_list[-1], self.rand_list[ind]
        #pop last
        self.rand_list.pop()
        
        print(self.rand_list,ind,self.rand_dict)
        
        if len(self.rand_list) > 1:
            #set new index
            print(ind)
            self.rand_dict[self.rand_list[ind]] = ind
            
        elif len(self.rand_list) == 1:
            self.rand_dict[self.rand_list[0]] = 0
            
        return True
        
    def getRandom(self) -> int:
        return self.rand_list[random.randint(0,len(self.rand_list)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

