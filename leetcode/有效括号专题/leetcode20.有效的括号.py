class Solution:
    # 替换法多种括号匹配{}()[]
    # 方法一
    def isValid(self, s: str) -> bool:
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''

    # 替换法多种括号匹配{}()[]
    # 方法二 用到栈
    def isValid1(self,s:str)->bool:
       if not s or len(s)==0:
           return True
       dist={'(':1,')':-1,'{':2,'}':-2,'[':3,']':-3}
       stack=[]
       for s1 in s:
           if len(stack)==0:
               stack.append(s1)
           elif dist[s1]+dist[stack[-1]]==0:
                stack.pop()
           else:
               stack.append(s1)
       return len(stack)==0

   # 方法三 用到栈
    def isValid1(self, s: str) -> bool:
       if not s or len(s) == 0:
           return True
       dist={'(':')',')':'(','{':'}','}':'{','[':']',']':'['}
       stack=[]
       for s1 in s:
           if not stack or dist[s1]!=stack[-1]:
               stack.append(s1)
           else:
               stack.pop()
       return True if not stack else False


    # 只有一种括号匹配问题（）（）
    def isValid2(self,s:str)->bool:
        if not s or len(s)==0:
            return True
        sum_=0
        for s1 in s:
            if s1=='(':
                sum_+=1
            else:
                if sum_==0:
                    return False
                else:
                    sum_-=1
        return sum_==0






