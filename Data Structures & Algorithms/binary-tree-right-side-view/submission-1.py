# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        q = deque()
        q.append(root)

       

        ans = []
        
        while q:
            temp = 0

            for _ in range(len(q)):


                front = q.popleft()

                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)
                temp = front.val
            ans.append(temp)
        return ans

