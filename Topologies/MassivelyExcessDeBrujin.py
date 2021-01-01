import numpy as np
import Math
# LLVM compiler
from numba import njit

@njit(parallel=True)
def MassivelyExcessDeBruijn(step):
  debrujin_cluster = np.zeros(shape=((7**step), (7**step)), dtype=np.int64)
  for i in range(0, 7 ** step):
    shl = Math.massive_shl(i, step)
    for s in shl:
      debrujin_cluster[i, s] = 1
      debrujin_cluster[s, i] = 1
  return debrujin_cluster

def TestMassivelyExcessDeBruijn():
  for step in range(2, 15):
    cluster = Math.MassivelyExceessDeBruijn(step)
    dist = Math.ToDistanceMatrix(cluster)
    D = Math.Diameter(dist)
    S = Math.Degree(cluster)
    AvgD = Math.AverageDiameter(dist)
    C = Math.Cost(cluster, dist)
    T = Math.Traffic(cluster, dist)
    print(
      "Step {}: Nodes {}, Diameter: {}, Degree {}, Average Diameter {}, Cost {}, Traffic {}".format(step, len(cluster),
                                                                                                    D, S, AvgD, C, T))
