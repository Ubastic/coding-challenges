class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        start = node = None

        while l1 or l2:
            if l1 is not None and (l2 is None or l1.val < l2.val):
                val = l1.val
                l1 = l1.next
            elif l2 is not None and (l1 is None or l2.val <= l1.val):
                val = l2.val
                l2 = l2.next
            else:
                break

            if start is None:
                start = node = ListNode(val)
            else:
                node.next = ListNode(val)
                node = node.next

        return start
