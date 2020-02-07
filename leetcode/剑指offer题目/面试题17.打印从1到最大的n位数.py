from typing import List

class Solution:
    def PrintToMaxOfDigits(self,n):
        if n<=0:
            return
        number=['0']*n

        while self.Increment(number)==False:

            self.Print(number)
    # 字符串相加
    def Increment(self,numbers:List[str]):
        isOverflow=False
        nTakeOver=0
        nLength=len(numbers)
        for i in range(nLength-1,-1,-1):
            #ord('a')=97
            nSum=ord(numbers[i])-ord('0')+nTakeOver
            if i==nLength-1:
                nSum+=1
            if nSum>=10:
                if i==0:
                    isOverflow=True
                else:
                    nSum-=10
                    nTakeOver=1
                    numbers[i]=str(nSum)
            else:
                numbers[i]=str(nSum)
                break
        return isOverflow

    def Print(self,number):
        length=len(number)
        flag=1
        s=''
        for i in range(length):
            if flag and number[i]!='0':
                flag=0
            if not flag:
                s+=number[i]

        print(s)


if __name__ == '__main__':
    s=Solution()
    s.PrintToMaxOfDigits(3)