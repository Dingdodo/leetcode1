"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import itertools
from typing import List

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res= []
        self.generateParenthesisIter('',n,n)
        return self.res
    def generateParenthesisIter(self,mstr,r,l):
        if r==0 and l==0:
            self.res.append(mstr)
            #如果左括号的个数还有剩余，则+’(‘然后递归
        if l>0:
            self.generateParenthesisIter(mstr+'(',r,l-1)
            #如果右括号有剩余且小于左括号的个数则+‘）’
        if r>0 and r>l:
            self.generateParenthesisIter(mstr+')',r-1,l)







if __name__=='__main__':
    s=Solution()
    res=s.generateParenthesis(2)

    print( res)

