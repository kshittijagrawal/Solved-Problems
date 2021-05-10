class Solution:
    def insert(self, intervals, newInterval):
        flag = 0
        for i, el in enumerate(intervals):
            if el[0] >= newInterval[0]:
                flag = 1
                intervals.insert(i, newInterval)
                break
        if flag == 0:
            intervals.append(newInterval)
        
        res = [intervals[0]]
        for i in intervals[1:]:
            if res[-1][1] >= i[0]:
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res.append(i)
        return res