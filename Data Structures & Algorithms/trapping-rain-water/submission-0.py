class Solution:
    def trap(self, height: List[int]) -> int:
        maxileft=[0]
        maxiright=[0]
        maxir=00
        maxil=00
        n=len(height)
        for i in range(1,n):
            if maxil<height[i-1]:
                maxil=height[i-1]
            maxileft.append(maxil)
        for i in range(n-2,-1,-1):
            if maxir<height[i+1]:
                maxir=height[i+1]
            maxiright.append(maxir)
        maxiright.reverse()
        water=0
        
        for i in range(n):
            water+=max(min(maxileft[i],maxiright[i])-height[i],0)
            
        return water


        