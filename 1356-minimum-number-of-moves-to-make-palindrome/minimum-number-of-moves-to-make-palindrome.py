class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        l, r, res, st = 0, len(s)-1, 0, list(s)
        while l < r:
            if st[l] != st[r]:
                i = r
                while i > l and st[l] != st[i]:
                    i -= 1
                if i == l:
                    st[i], st[i+1] = st[i+1], st[i]
                    res += 1
                    continue
                else:
                    while i < r:
                        st[i], st[i+1] = st[i+1], st[i]
                        i += 1
                        res += 1
            l, r = l+1, r-1
        return res


# At each point, we look at the first and the last elements
# if they are the same, then we skip them, else we find
# another element in the string that matches the left
# element and then we make the necessary swaps to move it
# to the right place. 
# if we can't find that element -- this means this is the middle element
# in the palindrome, we just move it one position to the right and continue
# over the next few iterations, it will be moved to the center automatically
# run it for string = "dpacacp", answer should be 4
# the character that should be in the middle is "d"