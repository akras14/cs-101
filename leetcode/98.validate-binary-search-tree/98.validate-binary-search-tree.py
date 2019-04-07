# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        if not root: return True
        
        def isValid(node, smallerThan, greaterThan):
            if smallerThan is not None and node.val >= smallerThan:
                return False
            if greaterThan is not None and node.val <= greaterThan:
                return False
            
            left = isValid(node.left, node.val, greaterThan) if node.left else True
            right = isValid(node.right, smallerThan, node.val) if node.right else True
            return left and right
        return isValid(root, None, None)
