import matplotlib.pyplot as plt
import numpy as np
import math
# LLVM compiler
from numba import njit


def Diameter(MA):
    max = np.max(MA)
    return max


def Degree(MA):
    return np.max([np.sum(A) for A in MA])


def AverageDiameter(MA):
    return np.sum(MA) / (len(MA) * (len(MA) - 1))


def Cost(MA, MD):
    return len(MA) * Diameter(MD) * Degree(MA)


@njit
def ToDistanceMatrix(MA):
    distance = np.zeros(shape=(len(MA), len(MA)), dtype=np.int64)
    distance = np.copy(MA)
    for i in range(len(MA)):
        for j in range(len(MA)):
            if distance[i, j] == 0:
                distance[i, j] = 9000000

    for k in range(len(MA)):
        for i in range(len(MA)):
            for j in range(len(MA)):
                if distance[i, j] > distance[i, k] + distance[k, j]:
                    distance[i, j] = distance[i, k] + distance[k, j]

    for i in range(len(MA)):
        distance[i, i] = 0
        for j in range(len(MA)):
            distance[j, i] = distance[i, j]

    return distance


def Traffic(MA, MD):
    return (2 * AverageDiameter(MD)) / Degree(MA)


def FloydPathReconstruct(MA):
    distance = np.zeros(shape=(len(MA), len(MA)), dtype=np.int64)
    distance = np.copy(MA)
    next = np.zeros(shape=(len(MA), len(MA)), dtype=np.int64)
    for i in range(len(MA)):
        for j in range(len(MA)):
            if distance[i, j] == 0:
                distance[i, j] = 9000000
            elif distance[i, j] == 1:
                next[i, j] = j
            elif i == j:
                distance[i, i] = 0
                next[i, i] = i

    for k in range(len(MA)):
        for i in range(len(MA)):
            for j in range(len(MA)):
                if distance[i, j] > distance[i, k] + distance[k, j]:
                    distance[i, j] = distance[i, k] + distance[k, j]
                    next[i][j] = next[i][k]

    for i in range(len(MA)):
        next[i, i] = i
        for j in range(len(MA)):
            next[j, i] = next[i, j]
    return distance, next


def Betweeness(MA):
    betweeness = [np.count_nonzero(MA == i) for i in range(len(MA))]
    return betweeness


def ToBetweenessVector(MA):
    distance = np.zeros(shape=(len(MA), len(MA)), dtype=np.int64)
    distance = np.copy(MA)
    betweeness = np.zeros(shape=(len(MA)), dtype=np.int64)
    for i in range(len(MA)):
        for j in range(len(MA)):
            if distance[i, j] == 0:
                distance[i, j] = 9000000

    for k in range(len(MA)):
        for i in range(len(MA)):
            for j in range(len(MA)):
                if distance[i, j] > distance[i, k] + distance[k, j]:
                    distance[i, j] = distance[i, k] + distance[k, j]
                    betweeness[k] = betweeness[k] + 1

    for i in range(len(MA)):
        distance[i, i] = 0
        for j in range(len(MA)):
            distance[j, i] = distance[i, j]

    return betweeness