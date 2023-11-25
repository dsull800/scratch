class Node:

    def __init__(self, key, val, next_node):
        self.key = key
        self.val = val
        self.next = next_node


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_tail = Node(None, None, None)
        self.lru_head = Node(None, None, self.lru_tail)
        self.lru_length = 1

    def get(self, key: int) -> int:
        lru_head = self.lru_head.next
        prev_node = self.lru_head
        while lru_head is not None:
            if lru_head.key == key:
                ret_val = lru_head.val
                if lru_head.next is not None:
                    getted_node = lru_head
                    if getted_node != self.lru_tail:
                        self.lru_tail.next = getted_node
                        self.lru_tail = getted_node
                        prev_node.next = getted_node.next
                        getted_node.next = None

                return ret_val
            prev_node = lru_head
            lru_head = lru_head.next
        return -1

    def put(self, key: int, value: int) -> None:
        prev_node = self.lru_head
        lru_head = self.lru_head.next
        self.lru_length += 1
        while lru_head is not None:
            if lru_head.key == key:
                if lru_head != self.lru_tail:
                    prev_node.next = lru_head.next
                    self.lru_tail.next = Node(key, value, None)
                    self.lru_tail = self.lru_tail.next
                else:
                    self.lru_tail.val = value

                self.lru_length -= 1
                return

            prev_node = lru_head
            lru_head = lru_head.next

        self.lru_tail.next = Node(key, value, None)
        self.lru_tail = self.lru_tail.next
        if self.lru_length > self.capacity:
            self.lru_length -= 1
            self.lru_head.next = self.lru_head.next.next

        # Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)