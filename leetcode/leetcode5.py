from audioop import reverse
import numpy as np

class Solution:
    def longestPalindrome(self, str):

        if len(str) == 0:
            return ""
        # if len(str)==1:
        #     return str
        res = []
        arr_s = []
        ans = []

        for j in range(len(str)):
            arr_s.append(str[j])
            if j == len(str):
                res.append([str[j]])
                break
            for i in range(len(str)-1,j,-1 ):
                if str[i] in arr_s:
                    for k in range(j+1,i+1):
                        arr_s.append(str[k])
                        res.append(arr_s)
                    break
                # else:
                #     arr_s.append(str[i])
            arr_s = []
        print(res)
        flag=0
        for arr in res:
            if all(np.array(arr) ==np.array(arr[::-1])):
                flag=1
            if flag==1:
                ans.append(arr)
                flag=0
        print(ans)
        res_str=""
        max=0
        m=0
        if len(ans)!=0:
            for i in range(len(ans)):
                if max<len(ans[i]):
                    max=len(ans[i])
                    m=i
            for s1 in ans[m]:
                res_str+=s1
        else:res_str=str[0]
        return  res_str
s=Solution()
s1="aaabaaaa"
res_str=s.longestPalindrome(s1)
print(res_str)
arr1=['a', 'b', 'a', 'd', 'a', 'd', 'a']
if all(np.array(arr1) == np.array(arr1[::-1])):
    print("kkkkk")