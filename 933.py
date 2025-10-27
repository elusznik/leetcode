class RecentCounter:

    def __init__(self):
        self.requests=[]

    def ping(self, t: int) -> int:
        count=0
        if self.requests and t-3000>=self.requests[-1]:
            self.requests.clear()
        self.requests.append(t)
        for req in self.requests:
            if req>=t-3000:
                count+=1
            else:
                del req
        return count

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)