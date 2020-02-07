class Solution(object):
    def merge(self, intervals):

       intervals=sorted(intervals,key=lambda x:x[1])

       for i in range(len(intervals)-1,0,-1):
           if intervals[i][0]<=intervals[i-1][1]:
               intervals[i-1][1]=intervals[i][1]
               intervals[i-1][0]=min(intervals[i][0],intervals[i-1][0])
               del intervals[i]

intervals= [[1,4],[4,5]]
mg=Solution()
intervals=mg.merge(intervals)
print(intervals)