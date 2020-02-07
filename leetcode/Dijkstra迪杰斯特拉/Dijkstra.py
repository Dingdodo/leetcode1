
# https://blog.csdn.net/newmemory/article/details/88614548
V=4
# 标记数组：used[v]值为False说明改顶点还没有访问过，在S中，否则在U中！
used=[False for _ in range(V)]
# distance[i] 表示从远点s 到i的最短距离
distance=[float('inf') for _ in range(V)]
# cost=[[float('inf')*V] for _ in range(V)]
# S只包含起点s；U包含除s外的其他顶点
def dijkstra(s):
    distance[s]=0
    while True:
        v=-1
        # 从未使用过的顶点中选择一个距离最小的顶点
        for u in range(V):
            if not used[u] and (v==-1 or distance[u]<distance[v]):
                v=u
        if v==-1:
            break
        used[v]=True
        for u in range(V):
            distance[u]=min(distance[u],distance[v]+cost[v][u])
if __name__ == '__main__':
   cost=[[float('inf')]*4 for _ in range(4)]
   print(cost)
   for _ in range(4):
       v,u,w=list(map(int,input().split(',')))
       cost[v][u]=w
   print(cost)
   s=int(input("请输入一个起点："))
   dijkstra(s)
   print(distance)



