class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l = r = 0
        n = len(intervals)
        output = []
        #[[1,3],[2,6], [2,9], [8,10],[15,18]]
        while r < n:
            if l == r:
                r += 1
                continue
            if intervals[l][1] >= intervals[r][0]:
                intervals[l][1] = max(intervals[r][1], intervals[l][1])
            else:
                output.append(intervals[l])
                l = r

            r += 1 
        output.append(intervals[l])
        return output
        
        
        
        
    