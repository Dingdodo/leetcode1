def bfs(adj,start):
    visited=set()
    que=[]
    que.append(start)
    while que:
        cur=que.pop()
        # print(cur)
        print(adj.get(cur,[]))
        for v in adj.get(cur,[]):
            if v not in visited:
                visited.add(v)
                que.append(v)
if __name__ == '__main__':
    graph={1:[4,2],2:[3,4],3:[4],4:[5]}
    bfs(graph,1)