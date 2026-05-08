class Solution:
    def reverseBits(self, n: int) -> int:
        ans=0
        k=31
        for i in range(32):
            ans+=(n&1)*(2**k)
            k-=1
            n=n>>1
        return ans
        