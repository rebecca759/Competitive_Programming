class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        cnt = 0

        for word in words:
            if self.is_stretchy(s,word):
                cnt += 1

        return cnt

    def is_stretchy(self,s,word):
        j = 0
        i = 0
        cnter1 = 0
        cnter2 = 0

        while i < len(word):
            if s[j] != word[i]:
                return False

            while j < len(s)-1 and s[j] == s[j+1]:
                j += 1
                cnter1 += 1
            
            while i < len(word)-1 and word[i] == word[i+1]:
                i += 1
                cnter2 += 1

            if cnter2 > cnter1 or (cnter2 != cnter1 and cnter1+1 == 2):
                return False
            
            cnter1 = cnter2 = 0
            i += 1
            j += 1

            if j == len(s) and i != len(word):
                return False

        return j >= len(s)