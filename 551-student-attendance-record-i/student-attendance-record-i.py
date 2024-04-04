class Solution:
    def checkRecord(self, s: str) -> bool:
        A_count = 0
        L_count = 0
        for i in s:
            if i == "A":
                A_count += 1
                if A_count == 2:
                    return False
            if i == "L":
                L_count += 1
                if L_count > 2:
                    return False
            else:
                L_count = 0
        return True