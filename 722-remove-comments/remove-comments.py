class Solution(object):
    def removeComments(self, source):
        res = []
        multi = False
        line = ''
        for s in source:
            i = 0
            while i < len(s):
                if not multi:
                    if s[i] == '/' and i < len(s) - 1 and s[i + 1] == '/':
                        break
                    elif s[i] == '/' and i < len(s) - 1 and s[i + 1] == '*':
                        multi = True
                        i += 1
                    else:
                        line += s[i]
                else:
                    if s[i] == '*' and i < len(s) - 1 and s[i + 1] == '/':
                        multi = False
                        i += 1
                i += 1
            if not multi and line:
                res.append(line)
                line = ''
        return res