class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap=[0]*2001
        for n in nums:
            hashmap[n+1000]+=1
        for i in range(len(hashmap)):
            hashmap[i]=(hashmap[i],i-1000)
        temp=sorted(hashmap)
        ans=[]
        for i in range(k):
            ans.append(temp[2000-i][1])
        return ans

        