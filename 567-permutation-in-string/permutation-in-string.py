class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n:
            return False
        
        s1_char_count = [0] * 26
        window_char_count = [0] * 26 # Window in s2

        # Populate list count.
        for i in range(m):
            s1_char_count[ord(s1[i]) - ord('a')] += 1
            window_char_count[ord(s2[i]) - ord('a')] += 1
        
        # Slide window across s2
        for i in range(m, n):
            if s1_char_count == window_char_count:
                return True

            window_char_count[ord(s2[i]) - ord('a')] += 1
            window_char_count[ord(s2[i - m]) - ord('a')] -= 1
            
        return s1_char_count == window_char_count