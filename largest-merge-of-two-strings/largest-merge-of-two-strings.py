class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:        
        res = []
        ind1, ind2, n1, n2 = 0, 0, len(word1), len(word2)
        
        while ind1 < n1 and ind2 < n2:
            if word1[ind1] > word2[ind2]:
                res.append(word1[ind1])
                ind1 += 1
            elif word1[ind1] < word2[ind2]:
                res.append(word2[ind2])
                ind2 += 1
            else:
                if word1[ind1:] > word2[ind2:]:
                    res.append(word1[ind1])
                    ind1 += 1
                else:
                    res.append(word2[ind2])
                    ind2 += 1
                    
        res.append(word1[ind1:])
        res.append(word2[ind2:])
            
        return "".join(res)
                