from heapq import heappop, heapify
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = dict(Counter(nums))
        heap = [[-val, -key] for key, val in c.items()]
        heapify(heap)
        result = []
        for _ in range(k):
            result.append(-heappop(heap)[1])
        return result