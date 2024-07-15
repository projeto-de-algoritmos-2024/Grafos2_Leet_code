from typing import List

class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        parent = list(range(n + 1))
        for i in range(threshold + 1, n + 1):
            for j in range(2 * i, n + 1, i):
                self.union(parent, j, i)
        return [self.find(parent, query[0]) == self.find(parent, query[1]) for query in queries]

    def find(self, parent: List[int], x: int) -> int:
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]

    def union(self, parent: List[int], x: int, y: int) -> None:
        rootX = self.find(parent, x)
        rootY = self.find(parent, y)
        if rootX != rootY:
            parent[rootY] = rootX


#class DSU:
#    def __init__(self, n):
#        self.parent = list(range(n))
#        self.rank = [1] * n    
#    def find(self, x):
#        if self.parent[x] != x:
#            self.parent[x] = self.find(self.parent[x])
#        return self.parent[x]    
#    def union(self, x, y):
#        rootX = self.find(x)
#        rootY = self.find(y)        
#        if rootX != rootY:
            # union by rank
#            if self.rank[rootX] > self.rank[rootY]:
#                self.parent[rootY] = rootX
#            elif self.rank[rootX] < self.rank[rootY]:
#                self.parent[rootX] = rootY
#            else:
#                self.parent[rootY] = rootX
#                self.rank[rootX] += 1
#    def connected(self, x, y):
#        return self.find(x) == self.find(y)
