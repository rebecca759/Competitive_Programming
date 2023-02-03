class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        
        while left < right:
            if s[left] != s[right]:
                return self.is_palindrome(s[left:right]) or self.is_palindrome(s[left+1:right+1])

            left += 1 
            right -= 1

        return True


    def is_palindrome(self,s):
        left = 0 
        right = len(s)-1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True