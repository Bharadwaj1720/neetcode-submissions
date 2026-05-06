class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if n%groupSize!=0:
            return False
        hand.sort()
        buckets=[]
        for i in range(n//groupSize):
            temp=set()
            buckets.append(temp)
        for i in range(n):
            for j in range(n//groupSize):
                if len(buckets[j])==0:
                    buckets[j].add(hand[i])
                    break
                if hand[i] not in buckets[j] and len(buckets[j])<groupSize:
                    if hand[i]-1 not in buckets[j]:
                        return False
                    buckets[j].add(hand[i])
                    break
        for i in range(n//groupSize):
            if len(buckets[i])!=groupSize:
                return False
        return True




        