class Node:
    def __init__(
        self,
        value: int,
        key: int,
        next=None,
        previous=None,
    ):
        self.value = value
        self.key = key
        self.next = next
        self.previous = previous


class LRUCache:

    def __init__(self, capacity: int):
        self.lru_cache: dict[int, Node] = {}
        self.max_capacity = capacity
        self.curr_size = 0

        self.head = None
        self.tail = None

    def _remove_node(self, node: Node) -> None:
        """
        Remove a node from the linked list.

        This DOES NOT remove it from the dictionary.
        """

        # Previous node should skip this node.
        if node.previous:
            node.previous.next = node.next
        else:
            # This node was the head.
            self.head = node.next

        # Next node should skip this node.
        if node.next:
            node.next.previous = node.previous
        else:
            # This node was the tail.
            self.tail = node.previous

        # Keep the new head clean.
        if self.head:
            self.head.previous = None

        # Disconnect the removed node completely.
        node.previous = None
        node.next = None

    def _append_node(self, node: Node) -> None:
        """
        Append a node to the MRU end (tail).
        """

        node.previous = self.tail
        node.next = None

        if self.tail:
            self.tail.next = node
        else:
            # Empty list.
            self.head = node

        self.tail = node

    def get(self, key: int) -> int:

        if key not in self.lru_cache:
            return -1

        node = self.lru_cache[key]

        # Already MRU.
        if node != self.tail:
            self._remove_node(node)
            self._append_node(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        # Existing key.
        if key in self.lru_cache:

            node = self.lru_cache[key]

            # Remove old node from list.
            self._remove_node(node)

            # Remove dictionary entry.
            self.lru_cache.pop(key)

            self.curr_size -= 1

        # Cache full.
        if self.curr_size == self.max_capacity:

            lru = self.head

            # Remove from list.
            self._remove_node(lru)

            # Remove from dictionary.
            self.lru_cache.pop(lru.key)

            self.curr_size -= 1

        new_node = Node(
            value=value,
            key=key,
        )

        self._append_node(new_node)

        self.lru_cache[key] = new_node

        self.curr_size += 1