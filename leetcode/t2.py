import itertools
import operator
from functools import reduce


def t2():
    sum1= 0
    n = int(input("n="))
    if n==0:
        return 0

    res_x=[]
    res_y=[]
    res=[]
    temp=[]

    for i in range(n):
        x = int(input("x="))
        y = int(input("y="))
        res_x.append(x)
        res_y.append(y)
        sum1+= x
    if sum1 % 2 != 0:
        print("员工总是数是偶数")
        return
    if n==1:
        return (x/2)*y

    M=sum1/2#有M份工作
    print(M)
    for x,y in zip(res_x,res_y):
        res.append([y]*x)
    res=reduce(operator.add, res)
    res=list(res)

    listx = []
    su = []
    iter = itertools.combinations(res, int(M))
    for i in iter:
        print(i)
        listx.append(i)
    s = set(listx)
    print(s)
    for t in s:
        print(list(t))
        su.append(list(t))
    for i in su:
        temp.append(sum(i))
    temp=sorted(temp)
    return temp[int(M)-1]



# lis=[8,5,5,2]
# listx=[]
# su=[]
# iter = itertools.combinations(lis,2)
# for i in iter:
#    listx.append(i)
# s=set(listx)
# for t in s:
#     su.append(sum(list(t)))
# su=sorted(su)
# print(su)

res=t2()
print(res)