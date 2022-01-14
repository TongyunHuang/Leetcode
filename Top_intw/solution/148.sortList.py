# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Supose n is the number of nodes in the linked list
- Start with splitting the list into sublists of size 1. Each adjacent pair of sublists of size 1 is merged in sorted order.
    - After the first iteration, we get the sorted lists of size 2. A similar process is reapeaded of a sublist of size 2
    - We use two pointers, mid and end that references to the start and end of second linked list
    - Merge the lists in sorted order
    - use tail to keep track of previous list and nextSubList for next list
"""

class Solution:
    def __init__(self):
        self.tail = ListNode()
        self.nextSubList = ListNode()
    # Function get called
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        n = self.getCount(head)
        start = head
        dummyHead = ListNode()
        size = 1
        while size < n:
            self.tail = dummyHead
            while start is not None:
                if start.next is None:
                    self.tail.next = start
                    break
                mid = self.split(start, size)
                self.merge(start, mid)
                start = self.nextSubList
            start = dummyHead.next
            size = size *2
        return dummyHead.next
    
    # find the ptr to start if second linked list
    def split(self, start, size):
        midPrev = start
        end = start.next
        idx = 1
        while idx < size and (midPrev.next is not None or end.next is not None):
            if end.next is not None:
                end = end.next.next if end.next.next is not None else end.next
            if midPrev.next is not None:
                midPrev = midPrev.next
            idx += 1
        mid = midPrev.next
        midPrev.next = None
        self.nextSubList = end.next
        end.next = None
        return mid # the start of second linked list
    
    # merge two list in sorted order
    def merge(self, list1, list2):
        dummyHead = ListNode()
        newTail = dummyHead
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                newTail.next = list1
                list1 = list1.next
                newTail = newTail.next
            else:
                newTail.next = list2
                list2 = list2.next
                newTail = newTail.next
                
        newTail.next = list1 if list1 is not None else list2
        # travse till the end of merged list to get the newTail
        while newTail.next is not None:
            newTail = newTail.next
        # link the old tail with the head of merged list
        self.tail.next = dummyHead.next
        # update the old tail to the new tail of merged list
        self.tail = newTail
    
    
            
            
    
        
    # count number of node in the linkedlist
    def getCount(self, head):
        cnt = 0
        ptr = head
        while ptr is not None:
            ptr = ptr.next
            cnt += 1
        return cnt
        

"""
Sol: Top-down merge sort
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
    
    def merge(self, left, right):
        dummyHead = ListNode()
        tail = dummyHead
        while left is not None and right is not None:
            if left.val < right.val:
                tail.next = left
                left = left.next
                tail = tail.next
            else:
                tail.next = right
                right = right.next
                tail = tail.next
        tail.next = left if left is not None else right
        return dummyHead.next
    
    def getMid(self, head):
        midPrev = None
        while head is not None and head.next is not None:
            midPrev = head if midPrev is None else midPrev.next
            head = head.next.next
        mid = midPrev.next
        midPrev.next = None
        return mid
"""
                