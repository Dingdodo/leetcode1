from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        print()

if __name__=="__main__":
    import numpy as np
    testMat= np.mat(np.eye(4))
    print(testMat[1,:])
    print(np.nonzero(testMat[:,1]>0.5)[0])

    mat0=testMat[np.nonzero(testMat[:,1]>0.5)[0],:]
    print(mat0)