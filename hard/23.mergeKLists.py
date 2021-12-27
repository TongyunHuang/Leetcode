# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists):
        """
    Idea
    - Pair up k lists and merhe each pair
    - After the first paring, k lists are merged into k/2 lists with avg 2N/k length, then k/4, k/8 and so on
    - Repeat this procedure until we get the final sorted linked list
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None
    
    def merge2Lists(self, list1, list2):
        #print(list1, list2)
        if list1 is None: return list2
        if list2 is None: return list1
        head = None
        last = None
        while list1 and list2:
            minNode, minList = None, 0
            if list1.val < list2.val:
                minNode, minList = list1, 1
                list1 = list1.next
            else:
                minNode, minList = list2, 2
                list2 = list2.next
            # setup ret val
            if head is None:
                head = minNode
                last = minNode
            else:
                last.next = minNode
                last = last.next
                last.next = None
        if list1 is not None:
            last.next = list1
        if list2 is not None:
            last.next = list2
        #print(head)
        return head
    
"""
# speed up merge2Lists: have a "fake head" and append directly from the head
    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next
"""