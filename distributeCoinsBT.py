# Time:O(n) 1 traversal
# Space:O(h) height of BT
# Leetcode: Yes
# Issues:


# dfs 0 ms
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0
        def dfs(root):
            nonlocal moves
            #basecase
            if not root:                    # basecase both chilrten null, return 0
                return 0
            # logic
            extras = root.val - 1           # current extra
            left = dfs(root.left)           # extra coins from left and right
            right = dfs(root.right)

            moves += abs(left+right+extras) # add total coins absolute

            return left+right+extras        # return l+r+e

        dfs(root)
        return moves
