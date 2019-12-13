from itertools import zip_longest


def all_nodes(l: ListNode):
    while l is not None:
        yield l.val
        l = l.next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ost, node = 0, None

        for a, b in zip_longest(all_nodes(l1), all_nodes(l2), fillvalue=0):
            n = a + b + ost
            n, ost = n % 10, n // 10

            if node is None:
                temp = node = ListNode(n)
            else:
                temp.next = ListNode(n)
                temp = temp.next

        if ost:
            temp.next = ListNode(ost)

        return node