# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: 'TreeNode') -> 'List[str]':
        if not root:
            return []
        answers = []
        def getPath(node, path):
            path = "" if path is None else path + "->"
            if node.left is None and node.right is None: 
                answers.append("{}{}".format(path,node.val))
            elif node.left is not None and node.right is None:
                getPath(node.left, "{}{}".format(path,node.val))
            elif node.left is None and node.right is not None:
                getPath(node.right, "{}{}".format(path,node.val))
            else:
                getPath(node.left, "{}{}".format(path,node.val))
                getPath(node.right, "{}{}".format(path,node.val))
        getPath(root, None)
        return answers
