# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
    def lowestCommonAncestor(self, root, p, q):
        """
        return True it is p or q
        if sum of two subtree and node itself is 2, then currNode is the LCA
        """
        self.findLCA(root, p, q)
        return self.ans
        
        
    def findLCA(self, root, p, q):
        # when LCA has been found
        if root is None:
            return False
        
        mid = 1 if root.val == p.val or root.val == q.val else 0
        left = 1 if self.findLCA(root.left, p, q) else 0
        right = 1 if self.findLCA(root.right,p,q) else 0
        
        if mid + left + right >= 2:
            self.ans = root
        return (mid+ left+right) >= 1
        
        
        