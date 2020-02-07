
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==0 or numRows==1:
            return s
        subNum=numRows-2
        array=[]
        substr=[]
        for i in range (0,len(s)//numRows):
             if i==0:
                 array.append(s[:numRows])
                 substr.append(s[numRows:numRows+subNum])
                 j=numRows+subNum
             else:
                 array.append(s[j:j+numRows])
                 substr.append(s[j+numRows:j+numRows+subNum])
                 j=j+numRows+subNum

        for i in range(array.count('')):
            array.remove('')
        for i in range(substr.count('')):
            substr.remove('')
        print(array)
        s_1=''
        for i in range(len(array[0])): #列
           for j in range(len(array)):#行
               s_1+=array[j][i]
        print(s_1)
        temp_s=[]
        for  st in substr:
             l=list(st)
             l.reverse()
             temp_s.append(l)

        print(temp_s)
        s_2=''
        for i in range(0,len(temp_s[0])):  # 行
               for j in range(0,len(temp_s)):  # 列
                  s_2+=temp_s[j][i]

        print(s_1)
        print(s_2)

        s_3=s_1[:len(array)+1]
        print(s_3)
        s_4=s_1[len(array)+1:]
        print(s_4)
        for i in range (len(s_4)):
            if i<len(s_2):
                s_3+=s_2[i]
            s_3+=s_4[i]

        print(s_3)

if __name__ == '__main__':
    s=Solution()
    s1="LEETCODEISHIRING"
    s.convert(s1,4)
    import tensorflow as tf
    message=tf.constant("welcome to the DNN")
    with tf.Session() as sess:
        print(sess.run(message).decode())