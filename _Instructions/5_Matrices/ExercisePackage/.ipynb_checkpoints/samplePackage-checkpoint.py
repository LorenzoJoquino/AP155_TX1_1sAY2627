import numpy as np
import matplotlib.pyplot as plt
import sys


def createZerosArray(rowZeros, columnZeros):
    return np.zeros((rowZeros, columnZeros))


def sumOf1ToN(n):
    return sum(np.arange(n+1))


def createBandedMatrix(shape, repeatingUnit, start, step):
    '''
    Creates a banded square matrix given the list of the repeating unit, the starting index\
    of the repeating unit in the top row, and the step of the starting index for the next row
    '''

    bandedMat = np.zeros(shape)
    rowInput = np.zeros(shape[1])
    rowInput[start:start+len(repeatingUnit)] = repeatingUnit
    for i in range(bandedMat.shape[0]):
        bandedMat[i] = rowInput
        rowInput = np.roll(rowInput, step)

    return bandedMat
    


def createJuncMatrixTriUni(N, Vplus, Vminus):
    '''
    Creates a matrix relating the current through the different junctions given a uniform,\
    triangular resistance network.\
    V_1 corresponds to index 0 in this matrix; V_2 --> index 1, etc. 
    '''

    matA = np.zeros((N,N))

    #Need to make this portion not hard coded
    matA[2:-2] = createBandedMatrix((N-4, N), [-1,-1,4,-1,-1], 0, 1)
    matA[0,0:3] = [3,-1,-1]
    matA[1,0:4] = [-1,4,-1,-1]
    matA[-2,-4:] = matA[1,0:4][::-1]
    matA[-1,-3:] = matA[0,0:3][::-1]
    
    vecW = np.zeros(N)
    vecW[0], vecW[1], vecW[-2], vecW[-1] = Vplus, Vplus, Vminus, Vminus

    return matA, vecW

def solveVoltage(matA, vecW):
    return np.linalg.solve(matA, vecW)

if __name__ == "__main__":
    #print("Hello World")
    #number = input("Enter a number: ")
    number = int(sys.argv[1])
    name = sys.argv[2]
    # print(f"The sum from 1 to {int(number)} is {sumOf1ToN(int(number))}.")
    print(f"The sum from 1 to {number} is {sumOf1ToN(number)}.")
    print(f"Your name is {name}")
    # print(f"{createZerosArray(int(number), int(number))}")