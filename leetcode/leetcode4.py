class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m=len(nums1)
        n=len(nums2)

        all=[]
        i=0
        j=0
        while i<m and j<n:
            if nums1[i]>=nums2[j]:
                all.append(nums2[j])
                j+=1
               
            else:
                all.append(nums1[i])
                i+=1

        if len(nums1)==i:
            for k in range(j,len(nums2)):
                all.append(nums2[k])
        else:
            for index in range(i, len(nums1)):
                all.append(nums1[index])

        if len(all)%2==0:
            return (all[(len(all)//2)]+all[(len(all)//2-1)])/2
        else:
            return all[(len(all) // 2)]

    def findMedianSortedArrays01(self, nums1, nums2):
        """
             :type nums1: List[int]
             :type nums2: List[int]
             :rtype: float
             """

        all_array=sorted((nums1+nums2))
        if len(all_array)%2==0:
            return (all_array[(len(all_array)//2)]+all_array[(len(all_array)//2-1)])/2
        else:
            return all_array[(len(all_array) // 2)]





s=Solution()
nums1=[]
nums2=[1]
res=s.findMedianSortedArrays01(nums1, nums2)
print(res)
