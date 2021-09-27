class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        count, container = 0, set()
        for i in range(len(emails)):
            local, domain = emails[i].split('@')
            res = []
            for j in range(len(local)):
                if local[j] == ".":
                    continue
                if local[j] == "+":
                    break
                res.append(local[j])
            
            count = count if "".join(res)+'@'+domain in container else count + 1
            container.add("".join(res)+'@'+domain)
        
        return count