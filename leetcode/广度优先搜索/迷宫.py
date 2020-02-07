import pandas as pd
def initMaze():
    """初始化迷宫"""
    # 使用列表解析式创建一个7*7的二维数组
    maze =[[0]*7 for i in range(7)]


    # 将四周设置为1，表示墙壁，老鼠的移动只在内部的5*5内
    for i in range(7):
        maze[0][i] = maze[-1][i] = 1
        maze[i][0] = maze[i][-1] = 1
    # 记录墙的位置
    walls = [(1,3),(2,1),(3,3),(3,4),(4,2),(5,4)]
    for i,j in walls:
        maze[i][j] = 1
    return maze

def printMaze(maze):
    for i in range(len(maze)):
        print(maze[i],end='\n')

def Dfs(start ,end ,maze):

    i,j=start #开始点（1，1）
    end_i,end_j=end #结束点（5，5）
    stack=[(i,j)] #定义栈
    maze[i][j]=1
    while stack:
        i,j=stack[-1]#取栈顶
        if (i,j)==(end_i,end_j):
            break #找到终点
        flag = 1
        for wi,wj in [(0,1),(1,0),(-1,0),(0,-1)]:
            if maze[i+wi][j+wj]==0:
               flag = 0
               maze[i + wi][j + wj]=1
               stack.append((i + wi,j + wj))
               break
        if flag==1:
            stack.pop()
    return stack




import numpy as np
#迷宫中0的位置代表墙，不能走
#8代表入口，1代表可走位置
#888代表出口
migong = '''
0	0	0	0	0	0	0	0	0	0
0	8	1	0	1	1	1	0	0	0
0	1	1	0	1	1	1	0	888	0
0	1	1	1	1	0	0	1	1	0
0	1	0	0	0	1	1	1	1	0
0	1	1	1	0	1	0	1	1	0
0	1	0	1	1	1	0	1	1	0
0	1	0	0	0	1	0	1	1	0
0	0	1	1	1	1	1	1	1	0
0	0	0	0	0	0	0	0	0	0'''

data = np.array(migong.split(), dtype = int).reshape((10,10))


def direction_set(data):
    # 找到data中未被走过的地方，并同时记录该地方能够走的地方
    sum_i,sum_j=np.where(data>0) #获取数组中大于0 的 下标 x一列数组 y一列数组
    print(sum_i)
    print(sum_j)
    dir_set={}

    for i ,j in zip(sum_i,sum_j):
        key=str(i)+str(j)

        for wi,wj in [(0,1),(1,0),(0,-1),(-1,0)]:
              if data[i+wi][j+wj]>0:  #向下走
                  if key in dir_set:
                     dir_set[key]+=[str(i+wi)+str(j+wj)]
                  else:
                     dir_set[key]=[str(i+wi)+str(j+wj)]
    return dir_set
    # if data[i][j+1]>0:  #向右走
    #     dir_set[key]=[str(i)+str(j+1)]
    # if data[i+1][j]>0:  #向下走
    #     if key in dir_set:
    #         dir_set[key]+=[str(i+1)+str(j)]
    #     else:
    #         dir_set[key]=[str(i+1)+str(j)]
    # if data[i][j-1]>0: #向上走
    #     if key in dir_set:
    #         dir_set[key]+=[str(i)+str(j-1)]
    #     else:
    #         dir_set[key]=[str(i)+str(j-1)]
    #
    # if data[i-1][j]>0: #向左走
    #     if key in dir_set:
    #         dir_set[key]+=[str(i-1)+str(j)]
    #     else:
    #         dir_set[key]=[str(i-1)+str(j)]
def get_forward_step(exit_index):
    layer_ori = ['11']   #存放第一层信息
    while True:
        layer_sec = []      #存放第二层信息
        for key in layer_ori: #将layer_ori里面所能达到的位置，存放在layer_sec中
            layer_sec += direction[key]
            if exit_index in direction[key]:
                forward_step = key
        if exit_index in layer_sec:
            break
        layer_ori = layer_sec
    return forward_step




if __name__ == '__main__':
    maze=initMaze()
    print(pd.DataFrame(maze))
    print(Dfs((1,1), (5,5), maze))

    direction = direction_set(data)
    print(direction)

    huish = ['28']
    # data[int(huish[0][0]), int(huish[0][1])] = 888 #将出口用888标记
    while True:
        forward_step = get_forward_step(huish[-1])
        huish += [forward_step]
        if forward_step == '11':
            break
    step = huish[::-1][:-1]
    for ind in step:
        data[int(ind[0]), int(ind[1])] = -8
    print(data)
    print(step)