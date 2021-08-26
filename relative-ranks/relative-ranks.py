class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        container = {num : ind+1 for ind, num in enumerate(sorted(score, reverse = True))}
        for i, s in enumerate(score):
            if container[s] == 1:
                score[i] = "Gold Medal"
            elif container[s] == 2:
                score[i] = "Silver Medal"
            elif container[s] == 3:
                score[i] = "Bronze Medal"
            else:
                score[i] = str(container[s])
        return score