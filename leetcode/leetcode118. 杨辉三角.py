from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows<1:
            return
        res=[]
        temp=[]
        for i in range(numRows):
            arr=temp
            temp=[]
            for j in range(i+1):
                if j==0 or j==i:
                    temp.append(1)
                    continue
                else:
                    temp.append(arr[j-1]+arr[j])
            res.append(temp)
        return res
if __name__ == '__main__':
    s=Solution()
    res=s.generate(5)
    print(res)