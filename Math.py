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

'''
def Betweeness(MA):
    betweeness = [np.count_nonzero(MA == i) for i in range(len(MA))]
    return betweeness
'''
@njit
def ToBetweenessVector(MA):
    distance = np.zeros(shape=(len(MA), len(MA)), dtype=np.int64)
    short_distance = np.zeros(shape=(len(MA), len(MA)), dtype=np.int64)
    distance = np.copy(MA)
    short_distance = np.copy(MA)
    betweeness = np.zeros(shape=(len(MA)), dtype=np.int64)
    for i in range(len(MA)):
        for j in range(len(MA)):
            if distance[i, j] == 0 and i != j:
                distance[i, j] = 9000000

    for k in range(len(MA)):
        for i in range(len(MA)):
            for j in range(len(MA)):
                if distance[i, j] > distance[i, k] + distance[k, j]:
                    distance[i, j] = distance[i, k] + distance[k, j]
                    short_distance[i, j] = distance[i, j]

    print(short_distance)

    for k in range(len(MA)):
        for i in range(len(MA)):
            for j in range(len(MA)):
                if (short_distance[i, j]) == (short_distance[i, k] + short_distance[k, j]) and i != j and k != j and k != i:
                    betweeness[k] = betweeness[k] + 1
                    if (i == 0 and j == 7):
                        print(str(i) + " " + str(k)+ " " + str(j))

    for b in range(len(betweeness)):
        print(str(b) + ": " + str(betweeness[b]))

    for i in range(len(MA)):
        distance[i, i] = 0
        for j in range(len(MA)):
            distance[j, i] = distance[i, j]

    return betweeness


def PrintProperties(step, cluster):
    dist = ToDistanceMatrix(cluster)
    D = Diameter(dist)
    S = Degree(cluster)
    AvgD = AverageDiameter(dist)
    C = Cost(cluster, dist)
    T = Traffic(cluster, dist)
    print(
      "Step {}: Nodes {}, Diameter: {}, Degree {}, Average Diameter {:.5f}, Cost {}, Traffic {:.5f}".format(step, len(cluster),
                                                                                                    D, S, AvgD, C, T))


def GetPropertiesString(step, cluster):
    dist = ToDistanceMatrix(cluster)
    D = Diameter(dist)
    S = Degree(cluster)
    AvgD = AverageDiameter(dist)
    C = Cost(cluster, dist)
    T = Traffic(cluster, dist)
    return  "Step {}: Nodes {}, Diameter: {}, Degree {}, Average Diameter {:.5f}, Cost {}, Traffic {:.5f}".format(step,
                                                                                         len(cluster), D, S, AvgD, C,T)

def ConvertToBase(num, base):
    q = num // base
    r = num % base
    if q == 0:
        return str(r)
    else:
        return ConvertToBase(q, base) + str(r)

def ConvertFromBaseSevenToExcessive(num):
    res = ''
    for s in str(num):
        if s == '4':
            res += ('T')
        elif s == '5':
            res += ('Z')
        elif s == '6':
            res += ('E')
        else:
            res += (s)
    return res

def ConvertFromBaseFiveToExcessive(num):
    res = ''
    for s in str(num):
        if s == '3':
            res += ('T')
        elif s == '4':
            res += ('Z')
        else:
            res += (s)
    return res

def ConvertFromBaseThreeToExcessive(num):
    res = ''
    for s in str(num):
        if s == '2':
            res += ('T')
        else:
            res += (s)
    return res

@njit
def massive_shl(number, digits):
  if(number * 7 < 7 ** digits):
    return (number * 7, number * 7 + 1, number * 7 + 2, number * 7 + 3, number * 7 + 4, number * 7 + 5, number * 7 + 6)
  elif (number * 7 - 2 * 7 ** digits < 0):
    return (number * 7 - 2 * 7 ** digits, number * 7 - 2 * 7 ** digits + 1, number * 7 - 2 * 7 ** digits + 2, number * 7 - 2 * 7 ** digits + 3, number * 7 - 2 * 7 ** digits + 4, number * 7 - 2 * 7 ** digits + 5,
            number * 7 - 2 * 7 ** digits + 6)
  elif (number * 7 - 3 * 7 ** digits < 0):
    return (number * 7 - 3 * 7 ** digits, number * 7 - 3 * 7 ** digits + 1, number * 7 - 3 * 7 ** digits + 2, number * 7 - 3 * 7 ** digits + 3, number * 7 - 3 * 7 ** digits + 4, number * 7 - 3 * 7 ** digits + 5,
            number * 7 - 3 * 7 ** digits + 6)
  elif (number * 7 - 4 * 7 ** digits < 0):
    return (number * 7 - 4 * 7 ** digits, number * 7 - 4 * 7 ** digits + 1, number * 7 - 4 * 7 ** digits + 2, number * 7 - 4 * 7 ** digits + 3, number * 7 - 4 * 7 ** digits + 4, number * 7 - 4 * 7 ** digits + 5,
            number * 7 - 4 * 7 ** digits + 6)
  elif (number * 7 - 5 * 7 ** digits < 0):
    return (number * 7 - 5 * 7 ** digits, number * 7 - 5 * 7 ** digits + 1, number * 7 - 5 * 7 ** digits + 2, number * 7 - 5 * 7 ** digits + 3, number * 7 - 5 * 7 ** digits + 4, number * 7 - 5 * 7 ** digits + 5,
            number * 7 - 5 * 7 ** digits + 6)
  else:
    return (number * 7 - 6 * 7 ** digits, number * 7 - 6 * 7 ** digits + 1, number * 7 - 6 * 7 ** digits + 2, number * 7 - 6 * 7 ** digits + 3, number * 7 - 6 * 7 ** digits + 4, number * 7 - 6 * 7 ** digits + 5,
            number * 7 - 6 * 7 ** digits + 6)

@njit
def ternaryexcess_shl(number, digits):
  if(number * 5 < 5 ** digits):
    return (number * 5, number * 5 + 1, number * 5 + 2, number * 5 + 3, number * 5 + 4)
  elif (number * 5 - 2 * 5 ** digits < 0):
    return (number * 5 - 2 * 5 ** digits, number * 5 - 2 * 5 ** digits + 1, number * 5 - 2 * 5 ** digits + 2, number * 5 - 2 * 5 ** digits + 3, number * 5 - 2 * 5 ** digits + 4)
  elif (number * 5 - 3 * 5 ** digits < 0):
    return (number * 5 - 3 * 5 ** digits, number * 5 - 3 * 5 ** digits + 1, number * 5 - 3 * 5 ** digits + 2, number * 5 - 3 * 5 ** digits + 3, number * 5 - 3 * 5 ** digits + 4)
  else:
    return (number * 5 - 4 * 5 ** digits, number * 5 - 4 * 5 ** digits + 1, number * 5 - 4 * 5 ** digits + 2, number * 5 - 4 * 5 ** digits + 3, number * 5 - 4 * 5 ** digits + 4)

@njit
def ternary_shl(number, digits):
  if (number * 3 < 3 ** digits):
      return (number * 3, number * 3 + 1, number * 3 + 2)
  elif (number * 3 - 2 * 3 ** digits < 0):
      return (number * 3 - 3 ** digits, number * 3 - 3 ** digits + 1, number * 3 - 3 ** digits + 2)
  else:
      return (number * 3 - 2 * 3 ** digits, number * 3 - 2 * 3 ** digits + 1, number * 3 - 2 * 3 ** digits + 2)
