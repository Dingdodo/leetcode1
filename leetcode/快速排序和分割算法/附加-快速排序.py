from typing import List
# 不稳地排序
def quickSort(arr_data:List[int],l,r):

   if l<r:
       i = l
       j = r
       temp = arr_data[l]
       while i!=j:
           while i<j and arr_data[j]>=temp:
               j-=1
           if i<j:
               arr_data[i]=arr_data[j]
               i+=1
           while i<j and arr_data[i]<=temp:
               i+=1
           if i<j:
               arr_data[j]=arr_data[i]
               j-=1
           arr_data[i]=temp
           quickSort(arr_data,l,i-1)
           quickSort(arr_data,i+1,r)


if __name__=="__main__":
  arr_data=[1,1,2,7,2,4]
  l,r=0,len(arr_data)-1
  quickSort(arr_data,l,r)
  print(arr_data)