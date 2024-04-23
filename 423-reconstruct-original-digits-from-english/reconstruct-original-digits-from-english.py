class Solution:
    def originalDigits(self, s: str) -> str:
        char_counts = {}
        for c in s:
            if c in char_counts:
                char_counts[c] += 1
            else:
                char_counts[c] = 1
                
        digit_counts = [0] * 10
        
        digit_counts[0] = char_counts.get('z', 0)
        digit_counts[2] = char_counts.get('w', 0)
        digit_counts[4] = char_counts.get('u', 0)
        digit_counts[6] = char_counts.get('x', 0)
        digit_counts[8] = char_counts.get('g', 0)
        
        digit_counts[1] = char_counts.get('o', 0) - digit_counts[0] - digit_counts[2] - digit_counts[4]
        digit_counts[3] = char_counts.get('h', 0) - digit_counts[8]
        digit_counts[5] = char_counts.get('f', 0) - digit_counts[4]
        digit_counts[7] = char_counts.get('s', 0) - digit_counts[6]
        digit_counts[9] = char_counts.get('i', 0) - digit_counts[5] - digit_counts[6] - digit_counts[8]
        
        return ''.join(str(i) * digit_counts[i] for i in range(10))