# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        from collections import deque
        queue = deque()
        start = head
        left = ListNode(val=None)
        while head is not None:
            if len(queue) == n:
                left = queue.popleft()
                queue.append(head)
            else:
                queue.append(head)
            head = head.next
        if len(queue) == n:
            if len(queue) >= 2:
                queue.popleft()
                left.next = queue.popleft()
            else:
                left.next = None
                start = left.val

        return start