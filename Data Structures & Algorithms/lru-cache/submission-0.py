class Node:
    def __init__(self, value: int, key: int, next=None, previous=None):
        self.value = value
        self.key = key
        self.next = next
        self.previous = previous


class LRUCache:

    def __init__(self, capacity: int):
        self.lru_cache: dict[int, Node] = {}
        self.max_capacity = capacity
        self.head = None
        self.tail = None
        self.curr_size = 0

    def get(self, key: int) -> int:
        if key not in self.lru_cache:
            return -1

        target_node = self.lru_cache[key]

        # BUG: If already the tail (MRU), don't move it.
        if target_node != self.tail:

            if target_node.previous:
                target_node.previous.next = target_node.next
            else:
                # BUG: You forgot that removing the head changes head.
                self.head = target_node.next

            if target_node.next:
                target_node.next.previous = target_node.previous

            # BUG: If the new head exists, its previous should become None.
            if self.head:
                self.head.previous = None

            target_node.previous = self.tail
            target_node.next = None

            if self.tail:
                self.tail.next = target_node

            self.tail = target_node

        return target_node.value

    def put(self, key: int, value: int) -> None:

        if key in self.lru_cache:
            curr_node = self.lru_cache[key]

            if curr_node.previous:
                curr_node.previous.next = curr_node.next
            else:
                # BUG: Existing node may be head.
                self.head = curr_node.next

            if curr_node.next:
                curr_node.next.previous = curr_node.previous
            else:
                # BUG: Existing node may be tail.
                self.tail = curr_node.previous

            # BUG: If head changed, clear previous.
            if self.head:
                self.head.previous = None

            self.lru_cache.pop(key)
            self.curr_size -= 1

        if self.curr_size == self.max_capacity:

            if self.head:

                self.lru_cache.pop(self.head.key)

                if self.head.next:
                    # BUG: This should be None, not False.
                    self.head.next.previous = None
                    self.head = self.head.next
                else:
                    # BUG: If removing the only node,
                    # tail must also become None.
                    self.head = None
                    self.tail = None

                self.curr_size -= 1

        new_node = Node(
            value=value,
            key=key,
            next=None,
            previous=self.tail,
        )

        if self.tail:
            self.tail.next = new_node

        self.tail = new_node

        # Correct.
        if not self.head:
            self.head = new_node

        self.lru_cache[key] = new_node
        self.curr_size += 1