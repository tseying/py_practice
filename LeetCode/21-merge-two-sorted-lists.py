# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

# =========================================
solution = Solution()
l1 = '1->2->4'
l2 = '1->3->4'
print solution.mergeTwoLists(l1, l2)