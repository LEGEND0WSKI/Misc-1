# Time:O(n) 1 traversal
# Space:O(d) depth of level
# Leetcode: Yes
# Issues:None


# bfs 0 ms
from collections import deque
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        q = deque()

        for i in nestedList:
            q.append(i)
        
        level = 1
        res = 0
        while q:
            n = len(q)
            for i in range(n):
                curr = q.popleft()

                if curr.isInteger():
                    res += level*curr.getInteger()
                else:
                    for i in curr.getList():
                        q.append(i)

            level +=1

        
        return res
# dfs 0 ms

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        return self.dfs(nestedList,1)

    def dfs(self,nestedList,depth):
        res = 0
        for ne in nestedList:
            if ne.isInteger():
                res += depth* ne.getInteger()
            else:
                res += self.dfs(ne.getList(),depth+1)
        return res

# dfs 2

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        self.res = 0

        self.dfs(nestedList, 1)

        return self.res

    def dfs(self,nestedList,depth):
        for ne in nestedList:
            if ne.isInteger():
                self.res += depth* ne.getInteger()
            else:
                self.dfs(ne.getList(),depth+1)
