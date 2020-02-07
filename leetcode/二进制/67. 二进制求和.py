class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1

        carry = 0
        ans = []
        while i >= 0 or j >= 0 or carry != 0:
            if i >= 0:
                carry += ord(a[i])-ord('0')
                i -= 1
            if j >= 0:
                carry += ord(b[j])-ord('0')
                j -= 1

            ans.append(str(carry % 2))
            carry >>= 1
        s = ''
        for i in range(len(ans) - 1, -1, -1):
            s += ans[i]
        return s
if __name__ == '__main__':
    s=Solution()
    a = "1010"
    b = "1011"
    print(s.addBinary(a,b))