class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i,j=len(num1)-1,len(num2)-1

        carry=0
        ans=[]
        while i>=0 or j>=0 or carry!=0:
            if i>=0:
                carry+=ord(num1[i])-ord('0')
                i-=1
            if j>=0:
                carry+=ord(num2[j])-ord('0')
                j-=1

            ans.append(str(carry%10))
            carry=carry//10
        s=''
        for i in range(len(ans)-1,-1,-1):
            s+=ans[i]
        return s
if __name__ == '__main__':
    s=Solution()
    ans=s.addStrings('56','47')
    s1='56'
    print(5+ord(s1[1])-ord('0'))
    print(ans)

