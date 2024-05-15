class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, x):
        node = self.root
        for i in range(18, -1, -1):
            bit = (x >> i) & 1
            node = node.setdefault(bit, {})
            node["mult"] = 1 + node.get("mult", 0)
        node["#"] = x

    def search(self, x):
        node = self.root
        for i in range(18, -1, -1):
            bit = (x >> i) & 1
            if 1 ^ bit in node: node = node[1 ^ bit]
            else: node = node[bit]
        return x ^ node["#"]

    def remove(self, x):
        node = self.root
        for i in range(18, -1, -1):
            bit = (x >> i) & 1
            node[bit]["mult"] -= 1
            if node[bit]["mult"] == 0:
                node.pop(bit)
                break
            node = node[bit]

class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        nodeQueries = {}
        for i, (node, val) in enumerate(queries):
            nodeQueries.setdefault(node, []).append([val, i])

        tree, root = {}, -1
        for node, parent in enumerate(parents):
            if parent == -1: root = node
            else: tree.setdefault(parent, []).append(node)
        
        res = [0] * len(queries)
        trie = Trie()

        def fn(node):
            trie.insert(node)
            for val, i in nodeQueries.get(node, []):
                res[i] = trie.search(val)
            for child in tree.get(node, []): fn(child)
            trie.remove(node)

        fn(root)
        return res
        