class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m_num = float('-inf')
        max_idx = -1
        smax = float('-inf')
        
        for i, num in enumerate(nums):
            if num > m_num:
                sec_max = m_num
                m_num = num
                max_idx = i
            elif num > sec_max:
                sec_max = num
                
        if m_num >= 2 * sec_max:
            return max_idx
        else:
            return -1