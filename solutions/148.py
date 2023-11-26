# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_next = head
        ll_length = 0
        while head_next:
            ll_length += 1
            head_next = head_next.next

        if ll_length <= 1:
            return head

        split = math.ceil(ll_length / 2)

        def merge_lists(list1, list2):
            new_node = TreeNode()
            orig_node = new_node
            while list1.val != float('inf') or list2.val != float('inf'):
                if list1.val < list2.val:
                    new_node.next = list1
                    list1 = list1.next if list1.next is not None else TreeNode(val=float('inf'))
                else:
                    new_node.next = list2
                    list2 = list2.next if list2.next is not None else TreeNode(val=float('inf'))
                new_node = new_node.next

            new_node.next = None
            return orig_node.next

        def split_lists(length, ll_list):
            if length == 1:
                return ll_list

            split = math.ceil(length / 2)
            first_head = ll_list

            split_count = 0
            second_head = first_head
            while second_head and split_count < split:
                split_count += 1
                prev_head = second_head
                second_head = second_head.next

            prev_head.next = None
            return merge_lists(split_lists(split, first_head), split_lists(length - split, second_head))

        return split_lists(ll_length, head)