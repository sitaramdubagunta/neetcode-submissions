# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        


        count = 0
        def dfs(root , currentmax):
            nonlocal count
            if not root:
                return

            
            if root.val >= currentmax:
                count += 1
                currentmax = root.val


            dfs(root.left , currentmax)
            dfs(root.right , currentmax)


        dfs(root , float('-inf'))

        return count
