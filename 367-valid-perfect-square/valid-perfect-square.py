class Solution(object):
    def isPerfectSquare(self, num):
        if num >= 0 and num < 2:
            return True
        else:
            i = 0
            j = 1
            while i <= num:
                if i == num:
                    return True
                i += j
                j += 2
            return False
        