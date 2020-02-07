#https://blog.csdn.net/sofuzi/article/details/81639795?utm_source=blogxgwz0
a=[1,2,3,4,5,6,7,8,9,3,10]
x1=0
for i in range(1,11):
    x1=(x1^i)
print(x1)
for j in range(11):
    x1=(x1^a[j])
print(x1)

class A:
    res = {}
    def __init__(self,x,y):
         self.x=x
         self.y=y

#  2x+y
    def compareTo(self):
        self.res[self]=[self.x,self.y]
        return self.res

if __name__ == '__main__':
  pass




