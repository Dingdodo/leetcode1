class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=1:
            return 0
        isPrimes=[1]*(n+1)
        isPrimes[0], isPrimes[1],cnt=0,0,0
        for i in range(2,n):
            if isPrimes[i]:
                for j in range(1,n+1):
                    if i*j<=n:
                       isPrimes[j*i]=0
                    else:
                        break
                cnt+=1
        return cnt





if __name__ == '__main__':
    s=Solution()
    count=s.countPrimes(10)
    print(count)
