# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.total = 0
        
        def backtrack(root, targetSum, total):
            if not root:
                return False
            total += root.val

            if not root.left and not root.right and total == targetSum:
                return True
            if backtrack(root.left, targetSum, total):
                return True
            
            if backtrack(root.right, targetSum, total):
                return True
            
            total -= root.val

            return False
    
        return backtrack(root, targetSum, self.total)