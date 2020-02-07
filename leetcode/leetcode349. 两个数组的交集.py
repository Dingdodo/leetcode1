from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 排序，去重，双指针
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        nums1 = sorted(list(set(nums1)))
        nums2 = sorted(list(set(nums2)))
        result = []

        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1
        return result
if __name__ == '__main__':
    s=Solution()
    nums1=[1,2,2,1]
    nums2=[2,2]
    res=s.intersection(nums1,nums2)
    print(set(nums1))
    print(set(nums1) & set(nums2))
