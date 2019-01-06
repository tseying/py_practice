# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        pre = head
        now = head.next
        while now is not None:
            if pre.val == now.val:
                now = now.next
                pre.next = now
            else:
                pre = pre.next
                now = now.next
        return head

        # if not head:
        #     return None
        # ptr = head
        # while ptr.next is not None:
        #     if ptr.val == ptr.next.val:
        #         ptr.next = ptr.next.next
        #     else:
        #         ptr = ptr.next
        # return head


# =========================================
solution = Solution()
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(2)
print solution.deleteDuplicates(head1)