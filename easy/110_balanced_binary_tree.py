# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        l = self.dfs_height(root.left)
        r = self.dfs_height(root.right)
                        
        diff = abs(l-r)
            
        if diff <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
    
    def dfs_height(self, node):
        if node == None:
            return 0
        
        leftHeight = self.dfs_height(node.left)+1
        rightHeight = self.dfs_height(node.right)+1
        
        return max(leftHeight, rightHeight)


