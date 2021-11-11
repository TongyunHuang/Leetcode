# MM/DD Jan 10

# Description
'''
Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists.
'''
# Method
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoLists( l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    # Edge case
    if l1 == None and l2 == None:
        return None
    elif l1 == None:
        return l2
    elif l2 == None:
        return l1
    # Initialize head
    h1, h2, head = l1, l2, ListNode()
    if h1.val < h2.val:
        head = h1
        h1 = h1.next
    else:
        head = h2
        h2 = h2.next
    # Main loop
    curr= head
    while h1 != None and h2!=None:
        if h1.val < h2.val:
            curr.next = h1
            h1 = h1.next
        else:
            curr.next = h2
            h2 = h2.next
        curr = curr.next
    # Handle tail
    if h1!= None:
        curr.next = h1
    elif h2!= None:
        curr.next = h2
    return head
# Test
'''
test =
print('your answer:')
print(test)
print('Compiler feedback:________')
assert(test==)
'''