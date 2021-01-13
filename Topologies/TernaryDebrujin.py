import numpy as np
import Math
# LLVM compiler
from numba import njit

@njit(parallel=True)
def TernaryDebrujin(step):
  debrujin_cluster = np.zeros(shape=((3**step), (3**step)), dtype=np.int64)
  for i in range(0, 3 ** step):
    shl = Math.ternary_shl(i, step)
    for s in shl:
      debrujin_cluster[i, s] = 1
      debrujin_cluster[s, i] = 1
  return debrujin_cluster


def TestTernaryDebrujin():
  for step in range(1, 12):
    cluster = TernaryDebrujin(step)
    dist = Math.ToDistanceMatrix(cluster)
    D = Math.Diameter(dist)
    S = Math.Degree(cluster)
    AvgD = Math.AverageDiameter(dist)
    C = Math.Cost(cluster, dist)
    T = Math.Traffic(cluster, dist)
    print(
      "Step {}: Nodes {}, Diameter: {}, Degree {}, Average Diameter {}, Cost {}, Traffic {}".format(step, len(cluster),
                                                                                                    D, S, AvgD, C, T))
