from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not (nums1 or nums2):
            return
        nums1=sorted(nums1)
        nums2=sorted(nums2)
        n=len(nums1)
        m=len(nums2)

        res=[]
        i=0
        j=0
        while i<n and j<m:
           if nums1[i]<nums2[j]:
               i+=1
           elif nums1[i]>nums2[j]:
               j+=1
           else:
               res.append(nums1[i])
               i+=1
               j+=1
        return res
if __name__ == '__main__':
    s=Solution()
    nums1=[1,2,2,1]
    nums2=[2]
    res=s.intersect(nums1,nums2)
    print(res)


