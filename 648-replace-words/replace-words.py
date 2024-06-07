class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        s=sentence.split(' ')
        d=dictionary
        ans=''

        for i in range(len(s)):
            for j in d:
                l=len(j)
                if s[i][0:l]==j:
                    s[i]=j

        for i in s:
            ans+=i+' '

        return ans.strip()
        

        
        
        

        
        