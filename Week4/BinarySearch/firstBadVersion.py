# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 0
        last = n
              
        while first <= last:
            mid = (first + last)//2
            
            if not isBadVersion(mid):
                first = mid+1
                
            else:
                if (mid > 0 and not isBadVersion(mid-1)):
                    return mid
                
                elif isBadVersion(mid-1):
                    last = mid-1
