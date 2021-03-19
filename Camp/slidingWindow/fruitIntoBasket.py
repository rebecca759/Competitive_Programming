class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        basket = {}
        
        max_fruits = 0
        fruits = 0
        
        left = 0
        right = 0
        
        while left < len(tree) and right < len(tree):
            if (tree[right] in basket):
                    basket[tree[right]] += 1
                    right += 1
                    
            elif len(basket) < 2:
                basket[tree[right]] = 1
                right += 1
                
            else:    
                max_fruits = max(max_fruits,right - left)
                basket[tree[left]] -= 1

                if basket[tree[left]] == 0:
                    basket.pop(tree[left])

                left += 1
                    
        max_fruits = max(max_fruits,right-left)
                    
        return max_fruits
                    
                
