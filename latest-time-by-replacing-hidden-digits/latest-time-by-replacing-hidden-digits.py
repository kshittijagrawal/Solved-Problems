class Solution:
    def maximumTime(self, time: str) -> str:
        res = [":"] * len(time)
        
        if time[0] != "?":
            res[0] = time[0]
        if time[0] == "?":
            if time[1] == "?" or int(time[1]) <= 3:
                res[0] = "2"
            else:
                res[0] = "1"
                
        if time[1] != "?":
            res[1] = time[1]
        if time[1] == "?":
            if res[0] == "2":
                res[1] = "3"
            else:
                res[1] = "9"
            
        if time[3] != "?":
            res[3] = time[3]
        if time[3] == "?":
            res[3] = "5"
            
        if time[4] != "?":
            res[4] = time[4]
        else:
            res[4] = "9"
            
        return "".join(res)