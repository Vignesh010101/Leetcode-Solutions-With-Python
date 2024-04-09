class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        myDict = set()
        for e in emails:
            local,domain = e.split('@')
            local = local.split('+')[0]
            local = local.replace('.','')
            myDict.add((local,domain))
        return len(myDict)