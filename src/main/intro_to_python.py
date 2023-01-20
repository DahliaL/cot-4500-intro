import numpy as np
import math

def printArray(arr):
    i, j = arr.shape
    
    if j == 3:
        for i in range(i):
            j = 0
            print(math.trunc(arr[i][j]), math.trunc(arr[i][j+1]), math.trunc(arr[i][j+2]))
    else:
         for i in range(i):
            j = 0
            print(math.trunc(arr[i][j]), math.trunc(arr[i][j+1]))
    
    print('\n')
    


prob1 = np.empty((3, 3))
prob2 = np.empty((3, 3))

# problem 1 and 2
for i in range(3):
    for j in range(3):
        if i==j:
            prob1[i][j] = 1
            prob2[i][j] = 1
        else:
            prob1[i][j] = 0
            prob2[i][j] = 3

printArray(prob1)

printArray(prob2)

prob3 = prob2[:,[0,1]]

printArray(prob3)



