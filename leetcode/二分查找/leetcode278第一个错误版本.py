# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return
        if n==1 and not isBadVersion(1):
            return 1
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)>>1
            if isBadVersion(mid):
                right=mid-1
            else:
                left=mid+1
        return left



