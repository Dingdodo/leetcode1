from typing import List


class Solution:
    def  quickSort(self,arr_data: List[int], l, r):
         if l<r:
             i=l
             j=r
             # 第一个点作为分割点
             temp=arr_data[l]
             while i !=j:
                 while i<j and arr_data[j]>=temp:
                     j-=1
                 if i<j:
                     arr_data[i]=arr_data[j]
                     i+=1
                 while i<j and arr_data[i]<=temp:
                     i+=1
                 if i<j:
                     arr_data[j]= arr_data[i]
                     j-=1

             arr_data[i]=temp
             self.quickSort(arr_data,l,i-1)
             self.quickSort(arr_data,i+1,r)



    def qSort(self,arr_data,left,right):

        def helper(arr_data,left,right):
            if left<right:
                i=self.position(arr_data,left,right)
                self.qSort(arr_data,left,i-1)
                self.qSort(arr_data,i+1,right)
        helper(arr_data,left,right)
        return arr_data
        # 确定排序一次的分界点的位置

    def position(self, arr_data: List[int], left, right):
        if not arr_data:
            raise Exception("无效数字", arr_data)


        i, j = left, right
        temp = arr_data[left]
        while i != j:
            # 后面j 开始走
            while i < j and arr_data[j] >= temp:
                j -= 1
            if i < j:
                arr_data[i] = arr_data[j]
                i += 1
            while i < j and arr_data[i] <=temp:
                i += 1
            if i < j:
                arr_data[j] = arr_data[i]
                j -= 1
        arr_data[i] = temp
        return i



    def qs(self,arr_data,left,right,k):
        if left<=right:
            i=self.position(arr_data,left,right)
            if i==k:
                return arr_data[i]
            elif i>k:
                return self.qs(arr_data,left,i-1,k)
            else:

                return self.qs(arr_data,i+1,right,k)

    def findKth(self,arr_data,k):
        # 第K大的数据下标
        return self.qs(arr_data,0,len(arr_data)-1,len(arr_data)-k)

if __name__ == '__main__':
    arr_data=[1,4,3,2]
    l,r=0,len(arr_data)-1
    s=Solution()
    s.quickSort(arr_data,l,r)
    print(arr_data)

    arr_data1 = [5, 4, 8, 1]
    # res=s.qSort(arr_data1,l,r)
    res=s.findKth(arr_data1,4)
    print(res)







