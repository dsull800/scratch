# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        orig_head = head
        length = 0
        if head is None:
            return None
        while head is not None:
            length += 1
            head = head.next

        k = k % length
        head = orig_head
        if k == 0:
            return head
        count = 0
        prev_node = None
        while head is not None:
            if count >= k:
                dummy = dummy.next
            count += 1
            prev_node = head
            head = head.next

        next_node = dummy.next
        dummy.next = None
        prev_node.next = orig_head
        return next_node

