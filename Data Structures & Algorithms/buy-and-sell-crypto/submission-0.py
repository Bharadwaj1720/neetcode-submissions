class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=100000
        maxi=0
        for i in prices:
            k=i-mini
            if k>maxi:
                maxi=k
            if mini>i:
                mini=i
        return maxi
        