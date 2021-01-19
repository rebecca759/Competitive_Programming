from collections import deque

class RecentCounter:
    def __init__(self):
        self.recent_requests = deque()

    def ping(self, t: int) -> int:
        request_count = 0
        
        self.recent_requests.appendleft(t)
        
        for time in self.recent_requests:
            if time < t-3000:
                break
                
            request_count += 1
                    
        return request_count
        
