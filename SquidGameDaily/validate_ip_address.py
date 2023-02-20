class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if self.valid_IPv4(queryIP):
            return "IPv4"
        elif self.valid_IPv6(queryIP):
            return "IPv6"
        else:
            return "Neither"

    def valid_IPv4(self,queryIP):
        nums = queryIP.split('.')

        if len(nums) != 4:
            return False

        for num in nums:
            if not num.isdigit():
                return False

            n = int(num)
            if not(0 <= n and n <= 255) or (num != '0' and num[0] == '0'):
                return False
        return True

    def valid_IPv6(self,queryIP):
        nums =  queryIP.split(':')

        if len(nums) != 8:
           return False


        for num in nums:
            if not(1 <= len(num) and len(num) <= 4):
                return False
            
            for n in num:
                n = n.lower()
                if not('a' <= n and n <= 'f') and not(n.isdigit()):
                    return False

        return True
    
