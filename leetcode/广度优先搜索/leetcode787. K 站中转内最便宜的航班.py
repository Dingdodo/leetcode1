from typing import List

from matplotlib import collections


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # dp[i][k]表示为经过k个中转站，到达第个i站的最低费用。
        dp=[[float('inf')]*(K+2) for _ in range (n)]
        # 选择的起点站 所有的k都赋值为0(相当于起点dp[0][k]--dp[0][K]一行都为0）
        for k in range(K+2):
            dp[src][k]=0
        # print(dp)
        for k in range(1,K+2):
            for flight in flights:
                if dp[flight[0]][k-1]!=float('inf'):
                    dp[flight[1]][k]=min(dp[flight[0]][k-1]+flight[2],dp[flight[1]][k])
        return -1 if dp[dst][K+1]==float('inf') else dp[dst][K+1]


def findCheapestPrice1(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    '''
    给人感觉是dij，但是竟然有一个k限制条件。。。
    但是其实就用bfs就好，上限是k，k到了还没到dst，就-1
    如果到了，就输出距离
    '''
    self.k = K
    self.dst = dst
    self.graph = collections.defaultdict(list)
    for u, v, w in flights:
        self.graph[u].append((v, w))
    print(self.graph)
    self.vis = [0] * n
    # Max=2**31
    self.dis = [-1] * n
    self.bfs(src)
    return self.dis[dst]
def bfs(self, src):
    q = []
    if not self.vis[src]:
        q.append((src, 0, self.k))
        self.vis[src] = 1
        self.dis[src] = 0
    while (q):
        curc, cost, k = q.pop(0)
        print(curc, cost, k)
        if k < 0:
            return -1
        for nextc, price in self.graph[curc]:
            if not self.vis[nextc] or (self.dis[nextc] != -1 and self.dis[nextc] > cost + price):
                self.vis[nextc] = 1
                self.dis[nextc] = cost + price
                q.append((nextc, cost + price, k - 1))

if __name__ == '__main__':
 s=Solution()
 n=3
 edges=[[0,1,100],[1,2,100],[0,2,500]]
 src=0
 dst=2
 K=0
 res=s.findCheapestPrice(n,edges,src,dst,K)
 print(res)
