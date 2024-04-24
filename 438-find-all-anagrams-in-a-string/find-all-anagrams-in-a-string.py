class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = len(p)
        mapper = {}
        def __mapper():
            nonlocal mapper
            for i in p:
                if i in mapper.keys(): mapper[i] += 1
                else: mapper[i] = 1
        __mapper()
        ans = []
        st = 0
        ed = 0
        while ed < len(s):
            if s[ed] in mapper.keys():
                mapper[s[ed]] -= 1
                if mapper[s[ed]] == 0:
                    del mapper[s[ed]]
                if not bool(mapper):
                    ans.append(st)
                    mapper[s[st]] = 1
                    st += 1
                ed += 1
            else:
                if st == ed:
                    st = ed = ed + 1
                else:
                    if s[st] in mapper.keys():
                        mapper[s[st]] += 1
                    else:
                        mapper[s[st]] = 1
                    st += 1
        return ans           