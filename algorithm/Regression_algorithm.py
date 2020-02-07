import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['simhei']

ex0=pd.read_table('ex0.txt', header=None)
# print(ex0.head())
# print(ex0.shape)
def get_Mat(dataSet):
    xMat=np.mat(dataSet.iloc[:,:-1])
    yMat=np.mat(dataSet.iloc[:,-1].values).T
    return  xMat,yMat

xMat,yMat=get_Mat(ex0)
print(xMat.A[:,1])
print(yMat.A)
def plotShow():
    xMat, yMat = get_Mat(ex0)
    plt.scatter(xMat.A[:,1],yMat.A,c='b',s=5)
    plt.show()
plotShow()