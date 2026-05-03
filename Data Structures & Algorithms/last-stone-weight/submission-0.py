import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones)>1:
            k1=heapq.heappop_max(stones)
            k2=heapq.heappop_max(stones)
            temp=abs(k1-k2)
            if temp!=0:
                heapq.heappush_max(stones,temp)
        if len(stones)==0:
            return 0
        return stones[0]