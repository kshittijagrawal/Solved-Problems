class Solution:
    def validIPAddress(self, IP: str) -> str:
        if "." not in IP and ":" not in IP:
            return "Neither"
        
        elif "." in IP:
            ourIP = IP.split(".")
            if not len(ourIP) == 4: return "Neither"
            for i in ourIP:
                if (not i.isdigit()) or (i=="") or (len(i)>1 and i[0]=="0"): return "Neither"
                if not 0 <= int(i) <= 255: return "Neither"
            return "IPv4"
        
        else:
            ourIP = IP.split(":")
            if not len(ourIP) == 8: return "Neither"
            for i in ourIP:
                if (not 1<=len(i)<=4): return "Neither"
                for j in i:
                    if (71<=ord(j)<=90) or (103<=ord(j)<=122): return "Neither"
            return "IPv6"