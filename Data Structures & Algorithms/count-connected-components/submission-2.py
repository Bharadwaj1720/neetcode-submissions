class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.edges=edges
        self.visited=set()
        count=0
        for i in range(n):
            if i not in self.visited:
                count+=1
                self.dfs(i)
        return count

    def dfs(self,i):
        self.visited.add(i)
        for j in self.edges:
            if j[0]==i and j[1] not in self.visited:
                self.dfs(j[1])
            if j[1]==i and j[0] not in self.visited:
                self.dfs(j[0])
        