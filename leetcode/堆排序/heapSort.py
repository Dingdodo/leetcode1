class Solution:

    def heapSort(self,nums):
        size=len(nums)
        self.build_heap(nums,size)
        for i in range(len(nums)-1,0,-1):
            temp=nums[0]
            nums[0]=nums[i]
            nums[i]=temp
            self.adjust(nums,0,i)

        return nums

    def build_heap(self,nums,size):
        for i in range(size//2,-1,-1):
            self.adjust(nums,i,size)

    # 大顶堆调整
    def adjust(self,nums,i,n):
        #左孩子
        left=2*i+1
        # 右孩子
        right=2*i+2
        # 父节点
        max_index=i
        if left<n and nums[max_index]<nums[left]:
            max_index=left
        if right<n and nums[max_index]<nums[right]:
            max_index=right
        if max_index!=i:
            temp=nums[i]
            nums[i]=nums[max_index]
            nums[max_index]=temp
            self.adjust(nums,max_index,n)

if __name__ == '__main__':
    nums=[-1,5,2,6,0,3,9,1,7,4]
    s=Solution()
    print(s.heapSort(nums))
