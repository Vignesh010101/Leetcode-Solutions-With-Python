class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordset=set(wordDict)
        result=[]

        def dfs(prefix: str, suffix: str) -> None:
            if suffix == '':
                result.append(prefix.rstrip())
            else:
                for i in range(len(suffix)):
                    if suffix[:i+1] not in wordset:
                        continue
                    dfs(prefix+suffix[:i+1]+' ', suffix[i+1:])

        dfs('',s)
        return result