# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        if root is None:
            return []
        que = deque()
        que.append(root)
        ans = []
        flag = 0
        while que:

            lvl_size = len(que)
            temp = []
            
            for _ in range(lvl_size):
                
                front = que.popleft()
                
                temp.append(front.val)
                
                if front.left:
                    que.append(front.left)

                if front.right:
                    que.append(front.right)
            if flag:
                ans.append(temp[::-1])
                flag = 0
            else:
                ans.append(temp)
                flag = 1

        return ans