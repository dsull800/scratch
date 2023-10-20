# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        counter = 1
        prev_node = ListNode(None, head)
        left_node = ListNode()
        right_node = ListNode()
        original_head = head
        if right == left:
            return head
        while head is not None:
            if counter == left:
                prev_node.next = right_node
                if prev_node.val == None:
                    original_head = right_node
                left_node.val = head.val
                new_node = left_node
            elif counter == right:
                right_node.next = new_node
                left_node.next = head.next
                right_node.val = head.val
                break
            elif left < counter < right:
                new_node = ListNode(head.val, new_node)

            counter += 1
            prev_node = head
            head = head.next

        return original_head