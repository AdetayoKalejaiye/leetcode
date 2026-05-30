# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = {}

        def postorder(node, count=0):
            if node is None:
                return
            if count in output:
                output[count].append(node.val)
            else:
                output[count] = [node.val]
            postorder(node.left, count + 1)
            postorder(node.right, count + 1)
            
        postorder(root)
        return list(output.values())