import numpy as np
import Math
from Topologies import TestTopology, MassivelyExcessDeBrujin as MEDB, TernaryDebrujin as Topo
import Modelling
# LLVM compiler
from numba import njit

def PrintResults(resArray):
    for res in resArray:
        print(res)


if __name__ == "__main__":
   # Math.PrintProperties(1, MEDB.TernaryExcessDeBruijn(2))

   # cluster = MEDB.TernaryExcessDeBruijn(2)
   # Math.PrintProperties(8, cluster)
   # betweeness = Math.ToBetweenessVector(cluster)

   # Math.PrintProperties(1, TestTopology.cluster_1)
    betweeness = Math.ToBetweenessVector(np.array(TestTopology.cluster_1))

    #res = Modelling.TestScenarios(cluster, betweeness, ceiling=0.3, coding=5)
    #PrintResults(res)