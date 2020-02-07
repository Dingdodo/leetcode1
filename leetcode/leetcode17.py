import itertools
from typing import List

"""
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digits_len=len(digits)
        if  digits_len==0:
            return ""
        res=[]
        dis={}
        dis['2']=['a','b','c']
        dis['3'] = ['d', 'e', 'f']
        dis['4'] = ['g', 'h', 'i']
        dis['5'] = ['j', 'k', 'l']
        dis['6'] = ['m', 'n', 'o']
        dis['7']=  ['p','q','r','s']
        dis['8'] = ['t', 'u', 'v']
        dis['9'] = ['w', 'x', 'y','z']

        res_arr=[]
        for s in digits:
            res_arr.append(dis[s])
        print(res_arr)

        temp=[]
        for x in itertools.product(*res_arr):
            temp.append(list(x))

        for s_arr in temp:
            s1=""
            for s2 in s_arr:
                s1+=s2
            res.append(s1)

        return res
s=Solution()
s.letterCombinations("23")



