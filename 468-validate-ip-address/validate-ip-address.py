class Solution:
    def validIPAddress(self, ip: str) -> str:
        ipv4=True
        for i in ip:
            if i=='.':
                break
            elif i==':':
                ipv4=False
                break
        if ipv4:
            arr=ip.split('.')
            if len(arr)!=4:return "Neither"
            for ele in arr:
                if ele=='':return "Neither"
                if len(ele)>1 and ele[0]=='0':
                    return "Neither"
                for i in ele:
                    if not i.isdigit():
                        return "Neither"
                if int(ele)>255:
                    return "Neither"
            return "IPv4"
        else:
            arr=ip.split(':')
            if len(arr)!=8:return "Neither"
            for ele in arr:
                if ele=='':return "Neither"
                if len(ele)>4:return "Neither"
                for i in ele:
                    if i.isalpha():
                        if i.lower() not in 'abcdef':
                            return "Neither"
                    elif i.isdigit():
                        pass
                    else:
                        return "Neither"
            return "IPv6"