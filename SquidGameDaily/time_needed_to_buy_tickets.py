class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        secs = 0
        val = tickets[0]
        

        while tickets[k] > 0: 
            for i,t in enumerate(tickets):
                if tickets[i] == 0:
                    continue
                if tickets[k] == 0:
                    return secs
                tickets[i] -= 1
                secs += 1

        return secs