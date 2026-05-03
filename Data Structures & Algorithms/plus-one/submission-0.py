class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        carry=1
        i=n-1
        while carry!=0 and i>=0:
            t=digits[i]+carry
            digits[i]=t%10
            carry=t//10
            i=i-1
            
        if carry==1:
            digits=[carry]+digits
        return digits

        