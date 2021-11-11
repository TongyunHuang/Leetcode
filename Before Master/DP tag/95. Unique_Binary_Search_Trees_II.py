
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        trees = []

        def constructTrees(start: int, end: int):
            l = []
            if start > end:
                l.append(None)
                return l
            for i in range(start, end+1):
                # smaller val go to the left
                leftSubtrees = constructTrees(start, i-1)
                # larger val go to the right
                rightSubtrees = constructTrees(i+1, end)

                for leftSub in leftSubtrees:
                    for rightSub in rightSubtrees:
                        node = TreeNode(i)
                        node.right = rightSub
                        node.left = leftSub
                        l.append(node)
            return l
        if n == 0:
            return []
        resL = constructTrees(1, n)
        return resL
