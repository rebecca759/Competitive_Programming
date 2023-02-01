class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mapping = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        res = set()
        
        for word in words:
            word2 = ''
            for c in word:
                word2 += mapping[ord(c)-ord('a')]
            res.add(word2)
        
        
        return len(res)