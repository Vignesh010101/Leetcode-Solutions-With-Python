class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = 0

class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        # Calculate the difference between the new value and the old value
        # for the given key, if it exists.
        diff = val - self.map.get(key, 0)
        self.map[key] = val
        
        # Traverse the Trie from the root to the node that represents
        # the prefix of the key, and update the node value with the new value.
        node = self.root
        node.value += diff
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.value += diff

    def sum(self, prefix: str) -> int:
        # Traverse the Trie from the root to the node that represents
        # the prefix, and return the value of that node.
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.value

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)