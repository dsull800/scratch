# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        counter = 0
        orig_head = head
        start_node = None
        end_node = ListNode()
        real_start = head
        while head is not None:
            if counter % k == 0:
                orig_start = head
                prev_end_node = end_node
                end_node = ListNode(head.val, None)
                new_node = end_node

            elif counter % k == k - 1:
                start_node = ListNode(head.val, new_node)
                prev_end_node.next = start_node
                if counter == k - 1:
                    real_start = start_node

            else:
                new_node = ListNode(head.val, new_node)

            head = head.next
            counter += 1

        if counter % k != 0:
            prev_end_node.next = orig_start

        return real_start

