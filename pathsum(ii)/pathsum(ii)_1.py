# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        output = []
        def traverse(node, count, path=[]):
            count += node.val
            path.append(node.val)
            if node.left is None and node.right is None:
                if count == targetSum:
                    output.append(path)
            if node.left:
                traverse(node.left, count, path.copy())
            if node.right:
                traverse(node.right, count, path.copy())
        if root:
            traverse(root, 0, [])
        return output
            
