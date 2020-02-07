from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=len(digits)-1
        carry=0
        ans=[]
        num2=[0]*len(digits)
        num2[-1]=1
        j=i
        while i>=0 or j>=0 or carry!=0:
            if i>=0:
                carry+=digits[i]
                i-=1
            if j>=0:
                carry+=num2[j]
                j-=1
            ans.append(carry%10)
            carry=carry//10
        return ans[::-1]
    # 第二种方法
    def plusOne1(self,numbers:List[int]):
        isOverflow=False
        nTakeOver=0
        nLength=len(numbers)
        for i in range(nLength-1,-1,-1):
            #ord('a')=97
            nSum=nTakeOver
            if i==nLength-1:
                nSum+=1
            if nSum>=10:
                if i==0:
                    isOverflow=True
                else:
                    nSum-=10
                    nTakeOver=1
                    numbers[i]=nSum
            else:
                numbers[i]+=nSum
                break
        return numbers
    # 方法3
    def  plusOne12(self,numbers:List[int]):

        n=len(numbers)-1
        for i in range(n,-1,-1):
            print(numbers[i])
            if numbers[i]!=9:
                numbers[i]+=1
                return numbers
            numbers[i]=0
        numbers[0]=1
        numbers.append(0)
        return numbers






if __name__ == '__main__':
    s=Solution()
    nums = [1, 9, 9]
    ans=s.plusOne(nums)
    print(ans)
    res=s.plusOne1(nums)
    print(res)
    nums = [1, 9, 9]
    arr=s.plusOne12(nums)
    print(arr)

