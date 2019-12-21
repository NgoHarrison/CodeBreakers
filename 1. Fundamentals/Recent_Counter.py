class RecentCounter:

    def __init__(self):
        self.queue=[]

    def ping(self, t: int) -> int:
        self.queue.append(t)                    #O(1)
        while self.queue[0] < t-3000:           #O(n)
            self.queue.pop(0)                   #O(1)
        return len(self.queue)                  #O(1)

#Overall time complexity is O(n)
#Overall space complexity is O(n) since I am using a list to store the pings

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
