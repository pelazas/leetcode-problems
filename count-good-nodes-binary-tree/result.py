# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Microsoft most asked question of 2021

        def dfs(node, max_val):
            if not node:
                return 0
            count = 0
            if node.val >= max_val:
                count = 1
            else:
                count = 0
            
            new_max = max(max_val, node.val)

            count+=dfs(node.left, new_max)
            count+=dfs(node.right, new_max)
            return count
        
        return dfs(root, root.val)
    
        
        
        