class Solution:
    def minOperations(self, logs: List[str]) -> int:
        c = 0
        while logs :
            log = logs.pop(0)
            match log :
                case "../" :
                    c = max(0, c - 1)
                    continue
                case "./" :
                    continue
            c += 1
        return c