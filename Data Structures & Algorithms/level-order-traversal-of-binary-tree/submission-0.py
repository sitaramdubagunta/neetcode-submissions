# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        if not root:
            return []
        q = deque()
        q.append(root)
        ans = []


        while q:


            
            level = []

            for _ in range(len(q)):
                front = q.popleft()
                left = front.left
                right = front.right

                if left:
                    q.append(left)
                if right:
                    q.append(right)

                level.append(front.val)
            ans.append(level)
        return ans


                