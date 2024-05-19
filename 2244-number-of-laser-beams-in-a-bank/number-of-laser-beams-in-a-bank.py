class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res=0
        prev=0
        
        for row in bank:
            dev=row.count('1')
            if dev>0:
                res+=dev*prev
                prev=dev
            
        return res