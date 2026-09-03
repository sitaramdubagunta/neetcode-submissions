# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self,root):

            if root is None:
                return 0


            left = root.left
            right = root.right
            self.maxheight = max(self.maxheight , self.height(left)+self.height(right))

            return 1 + max(self.height(left),self.height(right))
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.maxheight = 0

        
        self.height(root)
        
        return self.maxheight

