class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=[]
        for m in strs:
            temp=[0]*26
            for n in m:
                temp[ord(n)-ord('a')]+=1
            hashmap.append(temp)
        ans={}
        for m in range(len(hashmap)):
            key=''
            for i in range(len(hashmap[m])):
                
                if hashmap[m][i]!=0:
                    key+=str(hashmap[m][i])+chr(i+ord('a'))
                
            if key not in ans:
                ans[key]=[strs[m]]
            else:
                ans[key].append(strs[m])
        ans2=[]
        
        for value in ans.values():
            ans2.append(value)
        return ans2
        

        