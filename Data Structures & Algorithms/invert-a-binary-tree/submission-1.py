# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def node_switcher(self,node):
        node.left,node.right=node.right,node.left
        if node.left:
            self.node_switcher(node.left)
        if node.right:
            self.node_switcher(node.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            self.node_switcher(root)

        return root
        
        