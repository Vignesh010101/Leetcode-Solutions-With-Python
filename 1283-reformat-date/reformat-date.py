class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split(" ")
        ms = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        ds = day[:-2]
        mi = ms.index(month) + 1
        dn = f"0{ds}" if len(ds) < 2 else ds
        mn = f"0{mi}" if mi < 10 else  mi
        return f"{year}-{mn}-{dn}"