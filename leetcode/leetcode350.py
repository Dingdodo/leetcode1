class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        for s1 in nums1:
            if s1 in nums2:
              res.append(s1)
        return list(set(res))
s=Solution()
nums1 =  [4,9,5]
nums2 = [9,4,9,8,4]
res=s.intersect(nums1,nums2)
print(res)