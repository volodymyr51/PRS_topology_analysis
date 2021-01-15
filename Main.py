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
    #Math.PrintProperties(1, Topo.TernaryDebrujin(4))

    #cluster = Topo.TernaryDebrujin(4)
    #Math.PrintProperties(8, cluster)
    betweeness = Math.ToBetweenessVector(np.array(TestTopology.cluster_1))
    for b in range(len(betweeness)):
        print(str(b) + ':' + str(betweeness[b]))
    print(np.sum(betweeness))
    #res = Modelling.TestScenarios(cluster, betweeness, ceiling=0.3, coding=3)
    #PrintResults(res)