import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq =nums
        heapq.heapify(self.pq)
        while len(self.pq) > self.k:
            heapq.heappop(self.pq)

    def add(self, val: int) -> int:
        if len(self.pq) < self.k:
            heapq.heappush(self.pq,val)
        else:
            heapq.heappushpop(self.pq,val)
        return self.pq[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
