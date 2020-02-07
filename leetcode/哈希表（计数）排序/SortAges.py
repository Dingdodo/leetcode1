from typing import List
def SortAges(ages:List[int]):
   if not ages or len(ages)<=0:
       return
   length=len(ages)
   oldestAge=99
   timeOfAge=[0]*oldestAge

   for i in range(length):
       age=ages[i]
       if age<0 or age >oldestAge:

           print(age,"不符合年龄范围，退出")
           return
       timeOfAge[age]+=1#0到99每一个年龄出现的次数
   #统计
   index=0
   for i in range(oldestAge):
       for j in range(timeOfAge[i]):
           ages[index]=i
           index+=1

   return ages

if __name__ == '__main__':
    ages=[2,3,89,23,1,3,4,5,6,4,33,4,5,66,88]
    ages=SortAges(ages)
    print(ages)




