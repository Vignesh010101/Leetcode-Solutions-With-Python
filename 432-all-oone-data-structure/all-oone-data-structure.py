class Node:
    def __init__(self, key='', count=0):
        self.prev = None
        self.next = None
        self.count = count  # The number of times this key appears
        self.keys = {key}  # A set of keys with the same count

    def insert(self, node):
        """Insert the given node after this node."""
        node.prev = self
        node.next = self.next
        self.next.prev = node
        self.next = node
        return node

    def remove(self):
        """Remove this node from the list."""
        self.prev.next = self.next
        self.next.prev = self.prev


class AllOne:
    def __init__(self):
        self.root = Node()  # Dummy root node of the doubly linked list
        self.root.next = self.root  # Initialize root to point to itself
        self.root.prev = self.root
        self.nodes = {}  # Key to node dictionary

    def inc(self, key: str) -> None:
        """Increase the count of the key by 1."""
        if key not in self.nodes:
            # Key not in list, so add with count 1
            if self.root.next == self.root or self.root.next.count > 1:
                # Insert new node after root if next node's count is more than 1
                self.nodes[key] = self.root.insert(Node(key, 1))
            else:
                # Otherwise, add the key to the next node's keys
                self.root.next.keys.add(key)
                self.nodes[key] = self.root.next
        else:
            current = self.nodes[key]
            next_node = current.next
            if next_node == self.root or next_node.count > current.count + 1:
                # Insert new node if there's no node for count = current.count + 1
                self.nodes[key] = current.insert(Node(key, current.count + 1))
            else:
                next_node.keys.add(key)
                self.nodes[key] = next_node
            current.keys.discard(key)
            if not current.keys:
                # Remove current node if there are no keys left in it
                current.remove()

    def dec(self, key: str) -> None:
        """Decrease the count of the key by 1."""
        current = self.nodes[key]
        if current.count == 1:
            # Remove the key if its count goes to 0
            del self.nodes[key]
        else:
            previous = current.prev
            if previous == self.root or previous.count < current.count - 1:
                # Insert new node if there's no node for count = current.count - 1
                self.nodes[key] = previous.insert(Node(key, current.count - 1))
            else:
                # Otherwise, add the key to the previous node's keys
                previous.keys.add(key)
                self.nodes[key] = previous
        current.keys.discard(key)
        if not current.keys:
            # Remove current node if there are no keys left in it
            current.remove()

    def getMaxKey(self) -> str:
        """Return a key with the highest count. If no keys are present, return an empty string."""
        if self.root.prev == self.root:
            return ""  # The list is empty
        return next(iter(self.root.prev.keys))

    def getMinKey(self) -> str:
        """Return a key with the lowest count. If no keys are present, return an empty string."""
        if self.root.next == self.root:
            return ""  # The list is empty
        return next(iter(self.root.next.keys))

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()