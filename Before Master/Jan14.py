# MM/DD Jan 14

# Description
# Method
# 83. Remove Duplicates from Sorted List
class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head.next == None:
        return head
    curr, prev, count = head.next, head, 1
    while curr != None:
        if prev.val == curr.val:
            prev.next = curr.next
        else:
            prev = curr.val
        curr = curr.next
    return head

# 88. Merge Sorted Array
def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    while m-1 >= 0  and n-1 >=0:
        if nums1[m-1] > nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    if m == 0:
        while n-1 >=0:
            nums1[n-1] = nums2[n-1]
            n -= 1

# 100. Same Tree
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree( p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if not p and not q:
        return True
    if not p or not q:
        return False
    leftBool =  isSameTree(p.left, q.left)
    rightBool = isSameTree(p.right, q.right)
    if rightBool and leftBool and p.val == q.val:
        return True
    return False

# 101. Symmetric Tree
def isSymmetric(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root == None:
        return True
    return isSameTree2(root.left, root.right)
        
def isSameTree2(r1, r2):
    if not r1 and not r2:
        return True
    if not r1 or not r2:
        return False
    if r1.val != r2.val:
        return False
    l = isSameTree2(r1.left, r2.right)
    r = isSameTree2(r1.right, r2.left)
    return l and r

# 104. Maximum Depth of binary Tree
def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    l = self.maxDepth(root.left)+1
    r = self.maxDepth(root.right) +1
    return max(l,r)

# 107. 

# Test
node3 = ListNode(2, None)
node2 = ListNode(1, node3)
head = ListNode(1, node2)
test = deleteDuplicates(head)
print('your answer:')
print(test.val)
print(test.next.val)
print('Compiler feedback:________')
# assert(test==)
