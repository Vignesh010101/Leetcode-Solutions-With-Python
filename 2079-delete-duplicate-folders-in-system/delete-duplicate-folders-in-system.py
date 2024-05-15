class TrieNode:
    def __init__(self):
        self.children = {} # key is  or folder name, sub directories or the TrieNode is the value
        self.is_end = False # check if it is the child node of the tree
        self.deleted = False # True ifthe subtree should be deleted

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        
        # Setting Up a Basic trie Structure
        def insert(path):
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = TrieNode()
                node = node.children[folder]
            node.is_end = True
        
        # Serialize or hash the subfolders to find the duplicate ones
        def serialize(node):
            ans = '('
            for folder, child in sorted(node.children.items()):
                ans += folder + serialize(child)
            ans += ')'
            if ans != "()": 
                serialized[ans].append(node)
            return ans

        # Travers the trie and append non-duplicated folders to the result
        def dfs(node, path):
            if node.deleted:
                return
            if path:
                result.append(path)
            for folder, child in node.children.items():
                if not child.deleted:
                    dfs(child, path + [folder])

        # Step 1: Insert paths into the trie and build the Trie
        root = TrieNode()

        for path in paths:
            insert(path)
        
        #step 2: initiliaze the serialization and serilize the nodes
        serialized = defaultdict(list)
        serialize(root)
        # Step 3: Find the duplciated and mark them
        for nodes in serialized.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.deleted = True

        # Step 5: travers the trie and print the non duplicated sub trees
        result = []
        dfs(root, [])

        return result