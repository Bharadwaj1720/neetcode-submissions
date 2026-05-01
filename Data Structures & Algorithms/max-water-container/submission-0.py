class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p=0
        q=len(heights)-1
        maxi=000
        while p<q:
            k=min(heights[p],heights[q])*(q-p)
            if k>maxi:
                maxi=k
            if heights[p]<heights[q]:
                p+=1
            else:
                q-=1
        return maxi

        