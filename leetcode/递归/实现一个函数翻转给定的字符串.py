import sys
sys.setrecursionlimit(1000000)
# 明确函数是干什么的
# 寻找递归结束条件
# 第三要素：找出函数的等价关系式。
# 我们要不断缩小参数的范围，缩小之后，我们可以通过一些辅助的变量或者操作，使原函数的结果不变。
def reverString(s):
    if len(s)<=1:
        return s
    return reverString(s[1:len(s)])+s[0]
# 递归乘阶层
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

# 裴波那契数列
# 对于递归的问题，我们一般都是从上往下递归的，直到递归到最底，再一层一层着把值返回。
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-2)+fib(n-1)



if __name__ == '__main__':
    s='abcdf'

    # print(s[1:len(s)]+s[0])
    res=reverString(s)
    print(res)
    n=5
    ans=factorial(n)
    print(ans)
    ans1=fib(7)
    print(ans1)