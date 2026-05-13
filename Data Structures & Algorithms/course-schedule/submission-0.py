class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.visited=set()
        self.visiting=set()
        if len(prerequisites)==0:
            return True
        Flag=True
        for i in range(1,numCourses+1):
            if i not in self.visited:
                Flag&=self.dfs(prerequisites,i)
        return Flag



    def dfs(self,prerequisites,i):
        if i in self.visiting:
            return False
        self.visiting.add(i)
        Flag=True
        for j in prerequisites:
            if j[0]==i and j[1] not in self.visited:
                Flag&=self.dfs(prerequisites,j[1])
        self.visited.add(i)
        self.visiting.remove(i)
        return Flag

        