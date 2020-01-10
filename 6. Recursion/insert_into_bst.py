# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def helper(node, val):
    if node is None:
        return TreeNode(val)
    if val < node.val:
        node.left = helper(node.left,val)
    if val >= node.val:
        return helper(node.right,val)
    


class Solution:
    def insertIntoBST(self, node: TreeNode, val: int) -> TreeNode:
        
        if not node:
            return TreeNode(val)
        if val < node.val:
            node.left = self.insertIntoBST(node.left,val)
        else:
            node.right = self.insertIntoBST(node.right,val)
        return node
        
        
