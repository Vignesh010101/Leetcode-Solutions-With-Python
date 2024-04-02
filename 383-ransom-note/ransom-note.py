class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        str1,str2=Counter(ransomNote),Counter(magazine)
        if str1&str2==str1:
            return True
        return False