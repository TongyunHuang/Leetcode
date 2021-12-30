# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.d = {}
        self.level = 0
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Idea:
        when reach level L-1, if length of result array is not 2L-1, append empty array at both front and back
        discard empty array at the end
        """
        if root is None: return []
        self.levelOrder(root)
        res = []
        for i in range(-self.level, self.level+1):
            if self.d.get(i, None) is not None:
                res.append(self.d[i])
        return res
    
    def levelOrder(self, root):
        """
        traverse the tree in level order
        """
        self.d[0] = [root.val]
        last = [root]
        orderL = [0]
        width = len(last)
        level = 0
        
        while True:
            nextL = []
            nextO = []
            # go through each node in the last level
            for i in range(width):
                level = level+1
                # set up left node vertical order
                if last[i].left is not None:
                    order = orderL[i]-1
                    self.toVertical(last[i].left, order, level)
                    nextL.append(last[i].left)
                    nextO.append(order)
                # set up right node vertical order
                if last[i].right is not None:
                    order = orderL[i]+1
                    self.toVertical(last[i].right, order, level)
                    nextL.append(last[i].right)
                    nextO.append(order)
                    
            if len(nextL) == 0:
                break
            else:
                last = nextL
                orderL = nextO
                width = len(last)
        
    def toVertical(self, root, order, level):
        """
        add to vertical order dictionary
        """
        self.level = max(self.level, level)
        if self.d.get(order, None) is None:
            self.d[order] = [root.val]
        else:
            self.d[order].append(root.val)
        
        
            
            
            
            
        
        