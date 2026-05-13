class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.visited=[]
        self.visiting=set()
        if len(prerequisites)==0:
            return [i for i in range(numCourses)]
        Flag=True
        for i in range(numCourses):
            if i not in self.visited:
                Flag&=self.dfs(prerequisites,i)
        if Flag:
            return self.visited
        return []




    def dfs(self,prerequisites,i):
        if i in self.visiting:
            return False
        self.visiting.add(i)
        Flag=True
        for j in prerequisites:
            if j[0]==i and j[1] not in self.visited:
                Flag&=self.dfs(prerequisites,j[1])
        self.visited.append(i)
        self.visiting.remove(i)
        return Flag
        