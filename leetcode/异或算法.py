ary=[2,2,4,6]


res=0
#相同为0，不同为1
for i in ary:
    res^=i
print(res)