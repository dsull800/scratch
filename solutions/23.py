# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(list1, list2):
            start_node = ListNode()
            orig_node = start_node

            while list1 is not None and list2 is not None:
                if list1.val < list2.val:
                    start_node.next = list1
                    list1 = list1.next
                else:
                    start_node.next = list2
                    list2 = list2.next

                start_node = start_node.next


            if list2 is None:
                start_node.next = list1
                return orig_node.next

            if list1 is None:
                start_node.next = list2
                return orig_node.next

            return orig_node.next

        while len(lists) > 1:
            lists.append(merge(lists[0], lists[1]))
            if len(lists) >= 3:
                del lists[0]
                del lists[0]
        if len(lists):
            return lists[0]
        else:
            return None