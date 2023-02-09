class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)

        def recurse(cur,s):
            if len(cur)-1 == n+3 and len(s) == 0:
                res.append(cur[:len(cur)-1])
                return

            elif not is_valid_ip(cur) or len(s) == 0:
                return 

            for i in range(len(s)):
                if 0 <= int(s[:i+1]) <= 255 and (s[0] != '0' or len(s[:i+1]) == 1):
                    recurse(cur+s[:i+1]+".",s[i+1:])

        def is_valid_ip(ip):
            ip = ip.split('.')

            if len(ip) > 4:
                return False
            return True

        recurse('',s)
        return res