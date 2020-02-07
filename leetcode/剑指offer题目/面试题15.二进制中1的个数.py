# 方法一
def NumberOf1(n):
    count=0
    flag=1

    while flag<=n:
        if n&flag:
            count+=1
        flag=flag<<1
    return count

# 把一个整数减去1，再和原整数做与运算 只有1&1=1其他都是0
def NumberOf11(n):
    count=0
    while n:
        count+=1
        n=(n-1)&n

    return count


if __name__ == '__main__':


    print(NumberOf1(110))
    print(NumberOf11(110))

