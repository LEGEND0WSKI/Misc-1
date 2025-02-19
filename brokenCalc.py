# Time:O(log(n)) 
# Space:O(1)
# Leetcode: Yes
# Issues: None


# Greedy use / instead of * and + instad of -
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        count = 0

        while target > startValue:
            if target % 2 == 0:
                target = target//2
            else:
                target = target+1
            count+=1

        return count + (startValue - target) #1's 
        

# memory limt exceeded 1 -> 100000000
from collections import deque
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        q = deque()
        q.append(startValue)
        visited = set()
        visited.add(startValue)

        steps = 0
        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                if curr == target:
                    return steps
                if curr < target:
                    ne = curr*2
                    if ne not in visited:
                        visited.add(ne)
                        q.append(ne)
                if curr > 1:
                    ne = curr -1
                    if ne not in visited:
                        visited.add(ne)
                        q.append(ne)
            steps +=1


