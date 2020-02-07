class Solution:

    def countAndSay(self, n) -> int:
       """

       :type n: object
       """

       if n<=0:
           return n
       res=[-1]*(n+1)
       res[0]=0
       res[1]=1
       for i in range(2,n+1):
           res[i]=res[i-1]+res[i-2]
       return res[n]


if __name__=="__main__":
    s=Solution()
    print(s.countAndSay(6))
