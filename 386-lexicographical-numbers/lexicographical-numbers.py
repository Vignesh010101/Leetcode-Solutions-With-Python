class TriedNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self._root = TriedNode()
        self._lex_order = []

    @staticmethod
    def _reverse(num):
        rev = 0
        count = 0
        while num:
            rev = rev * 10 + num % 10
            num = num // 10
            count += 1 
        
        return rev, count

    def insert(self, number):
        curr = self._root

        rev, count = self._reverse(number)
        while count:
            # print(rev)
            n = rev % 10
            if n not in curr.children:
                curr.children[n] = TriedNode()
            
            curr = curr.children[n]
            rev = rev // 10 
            count -= 1
            

        curr.end = True

    def dfs(self):
        self._lex_order = []
        self._dfs(self._root, 0)
        return self._lex_order
    
    def _dfs(self, curr: TriedNode, val: int):

        if curr.end:
            self._lex_order.append(val)

        for v, child in curr.children.items():
            self._dfs(child, val * 10 + v)

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        trie = Trie()

        for n in range(1, n + 1):
            trie.insert(n)
        
        # trie.insert(10)
        return trie.dfs()



        