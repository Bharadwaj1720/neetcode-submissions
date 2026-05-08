import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        for i in points:
            dist=math.sqrt(i[0]**2 +i[1]**2)
            t=(dist,i[0],i[1])
            res.append(t)
        h=res[:k]
        heapq.heapify_max(h)
        print(res)
        for i in range(k,len(res)):
            print(res[i])
            heapq.heappush_max(h,res[i])
            heapq.heappop_max(h)
        ans=[]
        for i in range(k):
            t=heapq.heappop_max(h)
            ans.append([t[1],t[2]])
        return ans


        