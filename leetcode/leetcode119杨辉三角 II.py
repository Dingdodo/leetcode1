from typing import List

# C(k,i)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex<0:
            return
        res=[ ]
        temp=[]
        for i in range(rowIndex+1):
            arr=temp
            temp=[]
            for j in range(i+1):
                if j==0 or j==i:
                    temp.append(1)
                else:
                    temp.append(arr[j]+arr[j-1])
            res.append(temp)
        return  res[-1]
    # 方法2
    def getRow1(self, rowIndex: int) -> List[int]:
        if rowIndex<0:
            return
        res=[]
        n = self.fictoral(rowIndex)
        for i in range(rowIndex+1):
             m=self.fictoral(i)
             k=self.fictoral(rowIndex-i)
             res.append(n//(m*k))
        return res
    def fictoral(self,n):
        if n==1 or n==0:
            return 1
        return n*self.fictoral(n-1)












if __name__ == '__main__':
    s=Solution()
    # res=s.getRow(3)
    # print(res)
    res=s.getRow1(4)
    print(res)


