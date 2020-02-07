def isD(s:str):
    if not s or len(s)==0:
        return True

    if s[len(s)//2]!="&":
        return False

    stack=[]
    s_1=""
    for i in range(len(s)//2):
        s_1+=s[i]
        stack.append(s[i])

    s1=""
    while stack:
        s1+=stack.pop()
    if "&"in s1:
        return False
    s_2=''
    for j in range(len(s)//2+1,len(s)):
        s_2+=s[j]
        stack.append(s[j])
    print(s_2)
    s2=''
    while stack:
        s2+=stack.pop()
    if "&" in s2:
        return False
    return s1==s_2 and s2==s_1

if __name__ == '__main__':
    print(isD("a&&&a"))

