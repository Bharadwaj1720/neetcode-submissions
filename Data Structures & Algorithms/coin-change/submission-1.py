class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        self.ans=[]
        for i in range(amount+1):
            temp=['?']*n
            self.ans.append(temp)
        self.l(coins,amount,n-1)
        k=self.ans[amount][n-1]
        if k==100000:
            return -1
        return k

    def l(self,coins,amount,i):
        print(amount)
        if i==-1:
            return 100000
        if amount==0:
            self.ans[amount][i]=0
        elif self.ans[amount][i]!='?':
            return self.ans[amount][i]
        elif amount>=coins[i]:
            k1=self.l(coins,amount-coins[i],i)+1
            k2=self.l(coins,amount-coins[i],i-1)+1
            k3=self.l(coins,amount,i-1)
            self.ans[amount][i]=min(k1,k2,k3)
        else:
            k3=self.l(coins,amount,i-1)
            self.ans[amount][i]=k3
        return self.ans[amount][i]

        