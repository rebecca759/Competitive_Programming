class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a)-1
        j = len(b)-1
        summ = []
        carry = 0

        while i >= 0 or j >= 0:
            v1 = int(a[i]) if i >= 0 else 0
            v2 = int(b[j]) if j >= 0 else 0

            tot = carry
            tot += (v1+v2)
            summ.append(str(tot%2))

            carry = 1 if tot > 1 else 0

            j -= 1
            i -= 1

        if carry:
            summ.append('1')

        return "".join(summ[::-1])