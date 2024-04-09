class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        name = list(name)
        typed = list(typed)
        if name[0] != typed[0]:
            return False
        i = 1
        j = 1
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif name[i-1] == typed[j]:
                j += 1
            else:
                return False
        while j < len(typed):
            if name[i-1] == typed[j]:
                j += 1
            else:
                return False
        return i == len(name)