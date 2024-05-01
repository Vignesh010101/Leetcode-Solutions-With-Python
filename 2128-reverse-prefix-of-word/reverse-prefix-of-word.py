class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        vy=word.find(ch)
        if vy==-1:
            return word
        
        a=list(word[:vy+1])
        b=list(word[vy+1:])

        a.reverse()

        return "".join(a+b)