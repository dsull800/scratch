# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        candidate = head
        # dummy = ListNode(float(inf), None)
        prev_node = ListNode(float('-inf'))
        slow_node = ListNode(None, None)
        start_node = slow_node
        while head is not None:
            if not (candidate.val == prev_node.val or candidate.val == (
            head.next.val if head.next is not None else float(inf))):
                candidate = ListNode(candidate.val, None)
                slow_node.next = candidate
                slow_node = candidate

            prev_node = head
            head = head.next
            candidate = head

        return start_node.next
