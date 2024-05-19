class Solution:
    def minOperations(self, s: str) -> int:
        count01=0
        count10=0
        for i in range(0, len(s)):
            if(int(s[i])!=i%2):
                count01+=1
                count10=len(s)-count01

        return min(count01, count10)