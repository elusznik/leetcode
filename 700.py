# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        if val<node.val:
            if root.left:
                root = root.left
            else:
                return None
        elif val>node.val:
            if root.right:
                root = root.right
            else:
                return None
        elif val==node.val:
            return node
        return Solution.searchBST(self,root,val)