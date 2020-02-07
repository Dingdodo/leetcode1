class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda x: x[1])
        if len(intervals)==0:
            return [newInterval]
        elif len(newInterval)==0:
            return intervals
        intervals = sorted(intervals, key=lambda x: x[1])
        flag=0
        for i in range(len(intervals)-1,0,-1):
            if newInterval[1]>intervals[i][0]:
                flag=i
                break

