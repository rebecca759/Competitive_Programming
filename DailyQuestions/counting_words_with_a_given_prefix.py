class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt = 0
        for word in words:
            if self.is_prefix(word,pref):
                cnt += 1

        return cnt

    def is_prefix(self,word,prefix):
        if len(prefix) > len(word):
            return False
        is_prefix = True

        for i in range(len(prefix)):
            if prefix[i] != word[i]:
                is_prefix = False
                break

        return is_prefix