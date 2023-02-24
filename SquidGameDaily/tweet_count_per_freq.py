class TweetCounts:

    def __init__(self):
        self.tweets_dict = defaultdict(list)
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets_dict[tweetName].append(time)
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        # list of seconds for this tweet
        times = sorted(self.tweets_dict[tweetName])
        chunks = []
        val = 0
        #construct chunks
        if freq == "minute":
            val = 59
        elif freq == "hour":
            val = 3599
        else:
            val = 86399

        s,e = startTime,endTime

        while s+val <= endTime:
            chunks.append([s,s+val])
            s = s+val+1
        if s <= endTime:
            chunks.append([s,endTime])
        
        ind = 0
        res = [0 for _ in range(len(chunks))]

        for sec in times:
            chunk_start,chunk_end = chunks[ind]

            if chunk_start <= sec <= chunk_end:
                res[ind] += 1

            elif sec > chunk_end:
                while ind < len(chunks) and sec > chunk_end:
                    ind += 1
                    if ind < len(chunks):
                        chunk_start,chunk_end = chunks[ind]

                if ind < len(chunks) and chunk_start <= sec <= chunk_end:
                    res[ind] += 1
    
            if ind == len(chunks):
                break
        return res
        
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)