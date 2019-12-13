
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        start = node = None

        lists = [l for l in lists if l is not None]
        while lists:
            less = min(lists, key=lambda n: n.val)

            if start is None:
                start = node = ListNode(less.val)
            else:
                node.next = ListNode(less.val)
                node = node.next

            if less.next is None:
                lists.remove(less)
            else:
                lists[lists.index(less)] = less.next

        return start