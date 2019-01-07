#coding=utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
         """
        # if l1 is None and l2 is None:       #非递归的方法
        #     return None
        #
        # head = ListNode(0)      #创建一个新的链表，最后不return head而是return head.next
        # ptr = head
        #
        # while l1 is not None and l2 is not None:
        #     if l1.val < l2.val:
        #         ptr.next = l1
        #         l1 = l1.next
        #     else:
        #         ptr.next = l2
        #         l2 = l2.next
        #     ptr = ptr.next
        # if l1 is not None:
        #     ptr.next = l1
        # if l2 is not None:
        #     ptr.next = l2
        # return head.next


        #递归的方法
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val <= l2.val:
            head = l1
            head.next = self.mergeTwoLists(l1.next, l2)
        else:
            head = l2
            head.next = self.mergeTwoLists(l1, l2.next)
        return head

# =========================================
solution = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
print solution.mergeTwoLists(l1, l2)