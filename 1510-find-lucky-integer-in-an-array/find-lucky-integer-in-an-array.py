class Solution:
    def findLucky(self, arr: List[int]) -> int:
        max_num=-1
        for i in arr:
            if arr.count(i)==i:
                max_freq=i
                if max_num<max_freq:
                    max_num=max_freq
        return max_num