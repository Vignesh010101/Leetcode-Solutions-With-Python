class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans=""
        d={}
        for i in words:
            for j in i:
                ans=ans+code[ord(j)-97]
            d[ans]=i
            ans=""
        return(len((d.keys())))

        