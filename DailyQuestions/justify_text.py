class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        cur = []
        char_cnt = 0

        for i,word in enumerate(words):
            if char_cnt+len(cur)+len(word) > maxWidth:
                res.append(self.justify(cur,maxWidth,False,char_cnt))
                cur = []
                char_cnt = 0

            cur.append(word)
            char_cnt += len(word)

        if cur:
            res.append(self.justify(cur,maxWidth,True,char_cnt))

        return res

    def justify(self,words,width,is_last_line,cnt):
        if is_last_line or len(words) == 1:
            line = " ".join(words)
            diff = width-len(line)
            return line+(" "*diff)

        print(cnt)
        diff = width - (cnt+(len(words)-1))
        space = diff//(len(words)-1)
        rem = diff%(len(words)-1)
        line = ""

        for i in range(len(words)-1):
            line += (words[i]+" ")
            line += (" "*space)+(" "*(1 if rem else 0))
            print(line)
            if rem:
                rem -= 1

        print(words[-1])
        return line+words[-1]
