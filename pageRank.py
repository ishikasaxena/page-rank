import numpy as np
import math

# normalize the matrix (make it a probability matrix (all cols sum to 1))
def normalizeAdjacencyMatrix(A):
    n = len(A) # n = num of rows/cols in A
    for j in range(len(A[0])):
        sumOfCol = 0
        for i in range(len(A)):
            sumOfCol += A[i][j]
        
        if sumOfCol == 0: # adjust for dangling nodes (columns of zeros)
            for val in range(n):
                A[val][j] = 1/n
        else:
            for val in range(n):
                A[val][j] = (A[val][j] / sumOfCol)
    return A

# implement damping matrix using formula
# M = dA + (1-d)(1/n)Q, where Q is an array of 1's and d is the damping factor
def dampingMatrix(A):
    n = len(A) # n = num of rows/cols in A
    dampingFactor = 0.85
    Q = [[1/n]*n]*n
    arrA = np.array(A)
    arrQ = np.array(Q)
    arrM = np.add((dampingFactor)*arrA, (1-dampingFactor)*arrQ) # create damping matrix
    return arrM

# find eigenvector corresponding to eigenvalue 1
def findSteadyState(M, n):
    # find eigenvectors
    evectors = np.linalg.eig(M)[1]
    
    # find eigenvalues
    eigenValues = np.linalg.eig(M)[0]
    lstEVals = []
    for val in eigenValues:
        lstEVals.append(round(val))
    
    # find eigenvector with eigenvalue 1
    idxWithEval1 = lstEVals.index(1)
    steadyStateVector = evectors[:, idxWithEval1]
    
    # normalize steady state vector so its components sum to 1
    lstVersionSteadyState = []
    sumOfComps = 0
    returnVector = []
    for val in steadyStateVector:
        sumOfComps += val
        lstVersionSteadyState.append(val)
    for val in lstVersionSteadyState:
        returnVector.append(val/sumOfComps)
    
    return returnVector

def pageRank(A):
    n = len(A) # n = num of rows/cols in A
    A = normalizeAdjacencyMatrix(A) 
    M = dampingMatrix(A) 
    
    # find steady state vector
    steadyStateVectorOfA = findSteadyState(M, n)
    return steadyStateVectorOfA


# TEST CASES
print("\nPage Rank Examples")
# 1) (corresponds to directed graph (1) on readme.md)
matrix1 = [ [0, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 0] ]
print("1) matrix 1 = ", matrix1)
print("steady state vector: ")
print(pageRank(matrix1)) 
# expected output: [0.077, 0.054, 0.441, 0.429]

# 2)
matrix2 = [ [0, 0, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 0, 0, 1],
            [0, 0, 0, 0, 0, 1, 0, 0]  ]
print("\n2) matrix 2 = ", matrix2)
print("steady state vector: ")
print(pageRank(matrix2))
# expected output: [0.03037, 0.0536, 0.02735, 0.0617, 0.1621, 0.2836, 0.2419, .1393]
