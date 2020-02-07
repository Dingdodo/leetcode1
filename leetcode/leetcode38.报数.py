class Solution:
    def countAndSay(self, n: int) -> str:
        s="1"
        temp="1"
        for i in range(2,n+1):
            s=""
            count=1
            for j in range(1,len(temp)):
                if temp[j]==temp[j-1]:
                    count+=1
                else:
                    s+=str(count)
                    s+=temp[j-1]
            s+=str(count)
            s+=str(temp[len(temp)-1])
            temp=s
        return s

if __name__ == '__main__':
   s=Solution()
   s1=s.countAndSay(5)
   print(s1)

