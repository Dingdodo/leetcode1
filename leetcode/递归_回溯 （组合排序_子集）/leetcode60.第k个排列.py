import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n==0 or k<0:
            return
        nums=[ i+1 for i in range(n)]
        res=[]
        visted=[0]*n
        def helper(temp,length):
            if length==n:
                res.append(temp)
            for i in range(0,n):
                if visted[i]:
                    continue
                visted[i]=1
                helper(temp+[nums[i]],length+1)
                visted[i]=0
        helper([],0)
        s=''
        for i in res[k-1]:
            s+=str(i)
        return s ,res
    def getPermutation2(self, n: int, k: int) -> str:
        if n==0 or k<0:
            return
        nums=[i+1 for i in range(n)]
        res=''
        while nums:
            step = self.factorial(n-1)

            # 重点 去整上 K<step情况保证idx>=0
            idx = math.ceil(k /step)-1
            res+=str(nums[idx])
            nums.remove(nums[idx])
            n-=1
            # 整题的关键k下一步的走向
            k-=idx*step

        return res

    def factorial(self,n):
        if n==1 or n==0:
            return 1
        return n*self.factorial(n-1)


if __name__ == '__main__':
       s=Solution()
       # res,res1=s.getPermutation(4,9)
       # print(res1)
       # print(s.getPermutation2(3,3))
       # nums=[1,2,3]
       res=s.getPermutation2(4,9)
       print(res)






           

