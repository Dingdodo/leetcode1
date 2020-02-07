from typing import List

# 有一个容量为 N 的背包，要用这个背包装下物品的价值最大，这些物品有两个属性：体积 w 和价值 v。
#
# 定义一个二维数组 dp 存储最大价值，其中 dp[i][j] 表示前 i 件物品体积不超过 j 的情况下能达到的最大价值。设第 i 件物品体积为 w，价值为 v，根据第 i 件物品是否添加到背包中，可以分两种情况讨论：
#
# 第 i 件物品没添加到背包，总体积不超过 j 的前 i 件物品的最大价值就是总体积不超过 j 的前 i-1 件物品的最大价值，dp[i][j] = dp[i-1][j]。
# 第 i 件物品添加到背包中，dp[i][j] = dp[i-1][j-w] + v。
# 第 i 件物品可添加也可以不添加，取决于哪种情况下最大价值更大。因此，0-1 背包的状态转移方程为：
#

class Solution:
    def knapsack(self, W: int, N: int, weights: List[int], values: List[int]):
        # W = 15背包承受能力
        # N = 4 物品数量
        # weights = [3, 4, 5, 6] 物品的重量
        # values = [4, 5, 6, 7]  物品的价值
        dp=[[0]*(W+1) for _ in range(N+1)]
        for i in range(1,N+1):
            w=weights[i-1]
            v=values[i-1]
            for j in range(1,W+1):
                if j>=w:
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-w]+v)
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[N][W]
    def knapsack1(self,W:int,N:int,weights:List[int],values:List[int]):
        dp=[0]*(W+1)
        for i in range(N+1):
            w,v=weights[i-1],values[i-1]
            for j in range(W,0,-1):
                if j>=w:
                    dp[j]=max(dp[j],dp[j-w]+v)
        return dp[W]





    # https://www.bilibili.com/video/av36136952
    def knapsack2(self, W: int, N: int, weights: List[int], values: List[int]):
          # W重量
          # N件商品
          # dp[N][W] 表示前N个物品，剩下W空间 理解为前N个物品剩余W空间
          # 最多能装多少物品
          #比如dp[2][20],当我的背包容量有20kg的时候在0-2的编号物品 最多能装多少。
          dp=[[0]*(W+1) for _ in range(N+1)]
          for i in range(1,N+1):#物品的数量
              for j in range(1,W+1):#背包的承重量
                  if j<weights[i-1]:
                      # 当i的物品太重了，背包装不下，能装的就是前i-1件
                      dp[i][j]=dp[i-1][j]
                  else:
                      # 可选 可不选
                      # 不选情况dp[i][j]=dp[i-1][j]
                      # 选择的情况 dp[i][j]=dp[i-1][j-weights[i-1]]+values[i-1]
                      # 选择的情况装了前面的i-1件 那么空间变成了j-weights[i-1]但是价值多了values[i-1]
                      # 选择的情况装：前i-1件物品放入剩下的容量为j-weights[i-1]加上values[i-1]
                      dp[i][j]=max(dp[i-1][j],dp[i-1][j-weights[i-1]]+values[i-1])
          print(dp)
          return dp[N][W]
if __name__ == '__main__':
    s=Solution()
    W=15
    N=4
    weights=[3,4,5,6]
    values=[4,5,6,7]
    res=s.knapsack2(W,N,weights,values)
    print(res)

